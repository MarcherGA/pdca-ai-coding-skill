#!/usr/bin/env python3
"""
Track code quality metrics for PDCA AI coding sessions.

Usage:
    python track_metrics.py --repo /path/to/repo --since "7 days ago"
    python track_metrics.py --repo /path/to/repo --since "2024-01-01"
    python track_metrics.py --repo /path/to/repo --commits 50
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_git_command(repo_path, command):
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            command,
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e.stderr}", file=sys.stderr)
        return None


def get_commits(repo_path, since=None, count=None):
    """Get list of commit SHAs."""
    cmd = ["git", "log", "--format=%H"]
    
    if since:
        cmd.extend(["--since", since])
    if count:
        cmd.extend(["-n", str(count)])
        
    output = run_git_command(repo_path, cmd)
    if not output:
        return []
    return output.split('\n')


def get_commit_stats(repo_path, commit_sha):
    """Get stats for a single commit."""
    # Get changed files count
    files_cmd = ["git", "show", "--stat", "--format=", commit_sha]
    files_output = run_git_command(repo_path, files_cmd)
    if not files_output:
        return None
        
    lines = files_output.split('\n')
    file_changes = [l for l in lines if '|' in l]
    files_changed = len(file_changes)
    
    # Get lines changed
    stats_cmd = ["git", "show", "--shortstat", "--format=", commit_sha]
    stats_output = run_git_command(repo_path, stats_cmd)
    
    lines_changed = 0
    if stats_output:
        # Parse "X files changed, Y insertions(+), Z deletions(-)"
        parts = stats_output.split(',')
        for part in parts:
            if 'insertion' in part or 'deletion' in part:
                num = ''.join(filter(str.isdigit, part))
                if num:
                    lines_changed += int(num)
    
    # Check if commit includes both test and production files
    has_test_and_prod = False
    if file_changes:
        has_test = any('test' in f.lower() for f in file_changes)
        has_prod = any('test' not in f.lower() for f in file_changes)
        has_test_and_prod = has_test and has_prod
    
    return {
        'sha': commit_sha,
        'files': files_changed,
        'lines': lines_changed,
        'test_first': has_test_and_prod
    }


def calculate_metrics(commits_data):
    """Calculate quality metrics from commit data."""
    if not commits_data:
        return None
        
    total = len(commits_data)
    large_commits = sum(1 for c in commits_data if c['lines'] > 100)
    sprawling_commits = sum(1 for c in commits_data if c['files'] > 5)
    test_first_commits = sum(1 for c in commits_data if c['test_first'])
    
    total_files = sum(c['files'] for c in commits_data)
    total_lines = sum(c['lines'] for c in commits_data)
    
    return {
        'total_commits': total,
        'large_commit_pct': (large_commits / total * 100) if total else 0,
        'sprawling_commit_pct': (sprawling_commits / total * 100) if total else 0,
        'test_first_pct': (test_first_commits / total * 100) if total else 0,
        'avg_files_per_commit': total_files / total if total else 0,
        'avg_lines_per_commit': total_lines / total if total else 0,
        'large_commits': large_commits,
        'sprawling_commits': sprawling_commits,
        'test_first_commits': test_first_commits
    }


def print_metrics(metrics, targets):
    """Print metrics with color coding."""
    if not metrics:
        print("No metrics to display")
        return
        
    def status(value, target, lower_is_better=True):
        """Return emoji status based on target."""
        if lower_is_better:
            return "✅" if value <= target else "⚠️"
        else:
            return "✅" if value >= target else "⚠️"
    
    print("\n" + "="*60)
    print("PDCA CODE QUALITY METRICS")
    print("="*60)
    print(f"\nAnalyzed {metrics['total_commits']} commits\n")
    
    print("METRICS vs TARGETS:")
    print("-"*60)
    
    # Large commits
    status_icon = status(metrics['large_commit_pct'], targets['large_commit_pct'])
    print(f"{status_icon} Large Commits (>100 lines)")
    print(f"   Actual: {metrics['large_commit_pct']:.1f}% ({metrics['large_commits']} commits)")
    print(f"   Target: <{targets['large_commit_pct']}%\n")
    
    # Sprawling commits
    status_icon = status(metrics['sprawling_commit_pct'], targets['sprawling_commit_pct'])
    print(f"{status_icon} Sprawling Commits (>5 files)")
    print(f"   Actual: {metrics['sprawling_commit_pct']:.1f}% ({metrics['sprawling_commits']} commits)")
    print(f"   Target: <{targets['sprawling_commit_pct']}%\n")
    
    # Test-first discipline
    status_icon = status(metrics['test_first_pct'], targets['test_first_pct'], lower_is_better=False)
    print(f"{status_icon} Test-First Discipline")
    print(f"   Actual: {metrics['test_first_pct']:.1f}% ({metrics['test_first_commits']} commits)")
    print(f"   Target: >{targets['test_first_pct']}%\n")
    
    # Average files
    status_icon = status(metrics['avg_files_per_commit'], targets['avg_files'])
    print(f"{status_icon} Avg Files Per Commit")
    print(f"   Actual: {metrics['avg_files_per_commit']:.1f}")
    print(f"   Target: <{targets['avg_files']}\n")
    
    # Average lines
    status_icon = status(metrics['avg_lines_per_commit'], targets['avg_lines'])
    print(f"{status_icon} Avg Lines Per Commit")
    print(f"   Actual: {metrics['avg_lines_per_commit']:.1f}")
    print(f"   Target: <{targets['avg_lines']}\n")
    
    print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description='Track code quality metrics for PDCA AI coding'
    )
    parser.add_argument(
        '--repo',
        required=True,
        help='Path to git repository'
    )
    parser.add_argument(
        '--since',
        help='Analyze commits since this date/time (e.g., "7 days ago", "2024-01-01")'
    )
    parser.add_argument(
        '--commits',
        type=int,
        help='Analyze last N commits'
    )
    
    args = parser.parse_args()
    
    repo_path = Path(args.repo)
    if not repo_path.exists():
        print(f"Error: Repository path does not exist: {repo_path}", file=sys.stderr)
        sys.exit(1)
        
    if not (repo_path / '.git').exists():
        print(f"Error: Not a git repository: {repo_path}", file=sys.stderr)
        sys.exit(1)
    
    print("Fetching commits...")
    commits = get_commits(repo_path, since=args.since, count=args.commits)
    
    if not commits:
        print("No commits found matching criteria")
        sys.exit(0)
    
    print(f"Analyzing {len(commits)} commits...")
    commits_data = []
    for i, sha in enumerate(commits, 1):
        if i % 10 == 0:
            print(f"  Processed {i}/{len(commits)} commits...")
        stats = get_commit_stats(repo_path, sha)
        if stats:
            commits_data.append(stats)
    
    metrics = calculate_metrics(commits_data)
    
    # PDCA targets
    targets = {
        'large_commit_pct': 20,
        'sprawling_commit_pct': 10,
        'test_first_pct': 50,
        'avg_files': 5,
        'avg_lines': 100
    }
    
    print_metrics(metrics, targets)


if __name__ == '__main__':
    main()

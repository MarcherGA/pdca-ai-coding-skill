#!/usr/bin/env python3
"""
Initialize a new PDCA coding session with logging template.

Usage:
    python init_session.py "Feature name" --objective "Business objective"
    python init_session.py "JWT Auth" --objective "Add user authentication to API"
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path


SESSION_TEMPLATE = """# PDCA Session Log

**Session Date:** {date}
**Feature:** {feature}
**Estimated Time:** {estimated_time} hours

## Business Objective

{objective}

---

## ANALYSIS PHASE

### Approach Selected
[After analysis, document the chosen approach]

### Key Patterns Identified
[List the existing patterns we'll follow]

### Files to Modify
[List main files that will be touched]

---

## PLANNING PHASE

### Number of Steps
[X steps total]

### Checkpoints Planned
[After steps: X, Y, Z]

### Risk Flags
[Any identified risks or unknowns]

---

## IMPLEMENTATION NOTES

### Start Time
{start_time}

### Progress Log
[Track as you go - note interventions, deviations, learnings]

### Deviations from Plan
[Document when and why you deviated]

### Interventions Made
[Note when you had to redirect the AI]

### End Time
[Fill in when complete]

### Actual Duration
[Calculate total time]

---

## COMPLETION CHECK

### Status
[Complete / Needs Work]

### Tests Passing
[Yes / No - include count if available]

### Ready to Close
[Yes / No with reasoning]

### Outstanding Items
[List anything remaining]

---

## RETROSPECTIVE

### What Worked Well
[Top 2-3 things]

### What Could Be Better
[Top 2-3 improvements]

### Top Learning
[Single most valuable insight]

### Change for Next Time
[One specific action item]

### Quality Metrics
- Total commits: [#]
- Largest commit: [# lines]
- Files touched: [# files]
- Avg lines per commit: [#]
- Test-first discipline: [%]

---

## KNOWLEDGE CAPTURE

### Patterns Discovered
[Document any patterns learned about the codebase]

### Architecture Insights
[Any architectural learnings to share with team]

### Refactoring Opportunities
[Note any tech debt or improvement opportunities]

---

## PROMPT UPDATES

### Changes Made
[List any updates to prompt templates]

### Why
[Rationale for each change]

---

**Session Complete:** [Date/Time when finished]
"""


def create_session_log(feature, objective, output_dir, estimated_time=2):
    """Create a new session log file."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    
    # Create safe filename
    safe_feature = "".join(c if c.isalnum() or c in ('-', '_') else '_' 
                          for c in feature.lower())
    filename = f"session_{date_str}_{safe_feature}.md"
    
    # Fill in template
    content = SESSION_TEMPLATE.format(
        date=date_str,
        feature=feature,
        estimated_time=estimated_time,
        objective=objective,
        start_time=time_str
    )
    
    # Write file
    output_path = output_dir / filename
    output_path.write_text(content)
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Initialize a new PDCA coding session'
    )
    parser.add_argument(
        'feature',
        help='Name of the feature being implemented'
    )
    parser.add_argument(
        '--objective',
        required=True,
        help='Business objective for this session'
    )
    parser.add_argument(
        '--time',
        type=float,
        default=2.0,
        help='Estimated time in hours (default: 2)'
    )
    parser.add_argument(
        '--output',
        help='Output directory (default: current directory)'
    )
    
    args = parser.parse_args()
    
    output_dir = Path(args.output) if args.output else Path.cwd()
    if not output_dir.exists():
        print(f"Creating output directory: {output_dir}")
        output_dir.mkdir(parents=True)
    
    try:
        session_file = create_session_log(
            args.feature,
            args.objective,
            output_dir,
            args.time
        )
        print(f"\n✅ Session log created: {session_file}")
        print(f"\nNext steps:")
        print(f"1. Review Working Agreements")
        print(f"2. Load references/analysis-prompt.md")
        print(f"3. Fill in the session log as you progress")
        print(f"\nGood luck with your session! 🚀\n")
    except Exception as e:
        print(f"Error creating session log: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

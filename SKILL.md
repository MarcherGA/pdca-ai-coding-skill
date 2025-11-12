---
name: pdca-ai-coding
description: Structured Plan-Do-Check-Act framework for AI code generation with Claude Code or Cline. Use when implementing features, adding functionality, refactoring code, or any coding task that benefits from test-driven development, quality assurance, and continuous improvement. Prevents code quality issues, reduces debugging time, and maintains architectural consistency through structured prompts and human-AI collaboration.
---

# PDCA AI Coding Framework

Structured workflow for high-quality AI-assisted code generation using Plan-Do-Check-Act principles.

## When to Use This Skill

Use this skill for:
- Implementing new features (1-3 hour tasks)
- Refactoring existing code
- Adding integrations or cross-system functionality
- Any coding task requiring test-driven development
- Tasks where code quality and maintainability matter

**Do NOT use for:**
- Simple bug fixes (use lightweight version)
- Trivial changes that don't need testing  
- Exploratory coding or prototyping

## Quick Start

### Standard Mode (Guided, Phase-by-Phase)

Simply tell Claude what you want to implement:

```
I want to implement [your objective], let's use the PDCA framework
```

Claude will guide you through each phase, prompting you when to proceed to the next step. This is the default mode with full guidance and examples at each phase.

### Fast Mode (Streamlined, Single Load)

Add "fast mode" to your request:

```
I want to implement [your objective], let's use the PDCA framework fast mode
```

Claude will automatically load `references/fast-mode.md` and execute all 5 PDCA phases in one continuous workflow. **Saves 80% of loading time** while maintaining full quality.

**Note:** Working agreements are now inlined in all phase files - no separate load needed!

## Working Agreements (Summary)

**Full agreements in references/working-agreements.md - read before each session!**

**Note:** This skill works globally across all your projects. For project-specific configuration (tech stack, conventions), you can optionally create a `.claude/instructions.md` file in your project root. The Analysis phase will automatically check for and use this configuration. See the repository's `docs/PROJECT-CONFIGURATION.md` for details.

**Core Principles:**
- ✅ **Test-Driven Development**: Failing tests first, then production code
- ✅ **Incremental Change**: Small commits (<100 lines, <5 files)  
- ✅ **Respect Architecture**: Follow existing patterns
- ✅ **Human Accountability**: You own all AI-generated code

**Key Intervention Questions:**
- "Where's the failing test first?"
- "Are we fixing multiple things at once?"
- "Does this follow our patterns?"
- "Is this commit reviewable?"

See references/working-agreements.md for complete details.

## PDCA Workflow

### 1. Plan Phase - Analysis (2-10 min)

**Load the analysis prompt:**
\`\`\`
Load references/analysis-prompt.md and analyze: [your business objective]
\`\`\`

The AI will:
- Check for .claude/instructions.md (project configuration)
- Search codebase for existing similar patterns
- Document architectural context and abstractions
- Propose 2-3 alternative approaches with pros/cons
- Recommend the best approach

**Your actions:**
- Provide project context if requested (no .claude/instructions.md found)
- Review the analysis thoroughly
- Ask clarifying questions
- Provide additional context
- Approve the recommended approach
- Save analysis to project tracking (Jira, Linear, etc.)

### 2. Plan Phase - Task Breakdown (2 min)

**Load the planning prompt:**
\`\`\`
Load references/planning-prompt.md and create the execution plan
\`\`\`

The AI will:
- Break work into numbered, atomic TDD steps
- Define clear acceptance criteria for each step
- Set checkpoints every 3 steps for human review
- Flag risks and integration points

**Your actions:**
- Review the plan
- Adjust step order if needed
- Identify high-risk steps needing more attention
- Proceed to implementation

### 3. Do Phase - Implementation (variable, <3 hours)

**Load the implementation prompt:**
\`\`\`
Load references/implementation-prompt.md and execute the plan
\`\`\`

The AI will:
- Show reasoning before each step
- Write failing tests first (RED phase)
- Implement minimal production code (GREEN phase)
- Refactor while keeping tests green
- Commit after each successful batch

**Your actions:**
- Monitor AI reasoning for errors
- Intervene when context drifts
- Provide missing context when stuck
- Redirect if going off-plan
- Stop and replan if assumptions prove wrong
- Commit code after each step/batch

**Key intervention points:**
- When AI skips tests: "Stop. Write the failing test first."
- When changes too big: "This is too much. Break it into smaller steps."
- When context drifts: "Return to step X of the plan."
- When off-pattern: "This doesn't follow the [X] pattern we identified."

### 4. Check Phase - Completion Analysis (5 min)

**Load the completion check prompt:**
\`\`\`
Load references/completion-prompt.md and verify our work
\`\`\`

The AI will:
- Verify all tests pass and manual testing is complete
- Check code quality and test coverage
- Audit process adherence (TDD discipline maintained)
- Review architectural consistency
- Summarize accomplishments and deviations

**Your actions:**
- Review the completion analysis
- Spot-check code to verify claims
- Correct any inaccuracies
- Add completion analysis to project tracking
- Perform your own code review

### 5. Act Phase - Retrospective (2-10 min)

**Load the retrospective prompt:**
\`\`\`
Load references/retrospective-prompt.md and analyze our session
\`\`\`

The AI will:
- Summarize what was accomplished
- Identify critical moments that impacted success
- Flag wasted effort and wrong paths
- Highlight what worked well
- Suggest specific improvements for next time

**Your actions:**
- Read and reflect on findings
- Identify the ONE most valuable improvement
- Update prompt templates if needed
- Document patterns for future reference
- Note learnings in your personal knowledge base

## Complexity Variations

### Lightweight (Simple, Well-Patterned Tasks)

For implementing interfaces where clear examples exist:
- **Skip** detailed analysis (use existing patterns)
- **Simplify** planning (just TDD steps)
- **Keep** TDD discipline
- **Keep** retrospective

### Full Version (Complex, Cross-System Tasks)

For architectural changes, integrations, novel domains:
- **Full** analysis with alternatives
- **Detailed** planning with frequent checkpoints
- **Strict** TDD with human review
- **Comprehensive** completion check
- **Deep** retrospective

### Emergency Bug Fix

For production issues requiring immediate fixes:
- **Skip** analysis
- **Plan**: Reproduce bug + minimal fix + verification
- **TDD**: Write failing test exposing bug
- **Check**: Verify fix + no regressions
- **Act**: Document root cause and prevention

## Tracking Metrics

Use the metrics tracking script to measure quality:

\`\`\`bash
python scripts/track_metrics.py --repo /path/to/repo --since "7 days ago"
\`\`\`

Monitors:
1. Large commit % (>100 lines) - target: <20%
2. Sprawling commit % (>5 files) - target: <10%
3. Test-first discipline % - target: >50%
4. Avg files per commit - target: <5
5. Avg lines per commit - target: <100

## Session Logging

Track your sessions for continuous improvement:

\`\`\`bash
python scripts/init_session.py "Feature name" --objective "Business objective"
\`\`\`

This creates a session log in \`assets/session-template.md\` format to track:
- Analysis and plan decisions
- Implementation notes and interventions
- Completion verification results
- Retrospective learnings and improvements

## Tips for Success

### Context Management
- Keep sessions focused (1-3 hours)
- If context drifts, save and start new session
- Reference earlier analysis/plan to maintain coherence

### Effective Intervention
- Interrupt early when seeing reasoning errors
- Provide missing context proactively
- Ask clarifying questions for wrong assumptions

### Common Pitfalls to Avoid
- **Skipping analysis** → leads to code duplication and pattern violations
- **Skipping tests** → leads to regressions and debugging loops
- **Large batches** → harder to review, more likely to have issues
- **No retrospective** → miss improvement opportunities

### When to Replan
Stop and create a new plan if:
- Regression tests fail unexpectedly
- You discover missing context or wrong assumptions
- The approach proves more complex than anticipated
- Context drifts (off-pattern solutions emerge)

## Reference Files

All prompts and guidelines are in the \`references/\` directory:

**Fast Mode:**
- \`fast-mode.md\` - Complete PDCA workflow in one file (all phases consolidated)

**Standard Mode (Phase-by-Phase):**
- \`analysis-prompt.md\` - Detailed codebase analysis and approach selection
- \`planning-prompt.md\` - Task breakdown into TDD steps
- \`implementation-prompt.md\` - TDD execution guidelines
- \`completion-prompt.md\` - Quality verification checklist
- \`retrospective-prompt.md\` - Session learning and improvement

**Reference (Optional):**
- \`working-agreements.md\` - Complete core principles (now inlined in all prompts)

**When to Use Fast Mode vs Standard Mode:**
- **Standard Mode** ("let's use the PDCA framework"): Complex features, first-time users, when you want detailed guidance and examples
- **Fast Mode** ("let's use the PDCA framework fast mode"): Routine tasks, experienced PDCA users, when you want maximum efficiency

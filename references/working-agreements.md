# Working Agreements for Human-AI Collaboration

These are commitments the developer makes to engage and guide the AI agent according to a standard of quality.

## Purpose

Working agreements anchor human responsibility in AI collaboration and help maintain:
- Small batch sizes
- Coherent commits  
- Isolated pull requests
- Reduced coupling
- Better coherence
- Reduced code duplication

## Core Principles

### 1. Test-Driven Development (TDD)
- Write failing tests BEFORE production code
- Use behavioral failures, not compilation errors
- Create stub implementations that compile but fail behaviorally
- Verify tests pass after implementation

### 2. Incremental Change
- Small, atomic commits (<100 lines preferred)
- Touch fewer than 5 files per commit when possible
- One logical change per commit
- Coherent, reviewable changesets

### 3. Respect for Established Architecture
- Search for and follow existing patterns
- Use established abstractions before creating new ones
- Respect architectural layers and boundaries
- Match naming conventions

### 4. Human Accountability
- YOU are responsible for all code the AI produces
- Review AI reasoning at each step
- Intervene when seeing errors or drift
- Commit only code you understand and approve

## Intervention Questions

Ask yourself throughout the session:

**On Testing:**
- "Where's the failing test first?"
- "You're fixing multiple things, focus on one failing test?"
- "Is this test behavioral or just checking compilation?"

**On Scope:**
- "Is this commit too large to review easily?"
- "Are we changing too many files at once?"
- "Should this be split into smaller commits?"

**On Architecture:**
- "Does this follow our established patterns?"
- "Are we duplicating code instead of reusing?"
- "Have we searched for existing implementations?"
- "Are we respecting layer boundaries?"

**On Focus:**
- "Are we staying on plan?"
- "Is the AI going off on a tangent?"
- "Do we need to replan from here?"

## Quality Standards

### Commit Quality Targets
- **Large commits** (>100 lines): <20% of total
- **Sprawling commits** (>5 files): <10% of total
- **Test-first discipline**: >50% of commits include both test and production code
- **Average files per commit**: <5
- **Average lines per commit**: <100

### Code Quality Standards
- **Zero duplication**: Search before creating
- **Meaningful tests**: Test behavior, not implementation
- **Real components**: Prefer real over mocks when possible
- **Clear naming**: Follow project conventions
- **Documented "why"**: Comments explain rationale, not mechanics

## Session Discipline

### Before Starting
- Read these agreements (1 minute)
- Clear business objective defined
- Ready to actively supervise

### During Implementation
- Watch AI reasoning for errors
- Intervene early when drift detected
- Provide context proactively
- Keep sessions focused (<3 hours)

### After Completion
- Review completion analysis
- Verify quality claims
- Conduct retrospective
- Update prompts based on learnings

## Why These Matter

These agreements help you:
- ✅ Maintain quality with AI assistance
- ✅ Stay accountable for generated code
- ✅ Prevent common AI coding pitfalls
- ✅ Create reviewable, maintainable code
- ✅ Continuously improve your process

Read these before EVERY coding session to reset your mindset and intentions.

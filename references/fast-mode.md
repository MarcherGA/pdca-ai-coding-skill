# PDCA Fast Mode - Complete Workflow

**For experienced users:** This file consolidates all PDCA phases into a single prompt. Load once and execute the complete workflow.

**Use standard mode if:** This is your first time using PDCA, the task is highly complex, or you need detailed guidance at each phase.

## Working Agreements (Quick Reference)

**Core Principles:**
- ✅ **Test-First**: Failing tests before production code (behavioral failures, not compilation errors)
- ✅ **Small Commits**: <100 lines, <5 files, one logical change
- ✅ **Follow Patterns**: Search and reuse existing abstractions
- ✅ **You Own It**: Review AI reasoning, intervene early, commit only what you understand

**Key Interventions:**
- "Where's the failing test first?"
- "Is this commit too large/touching too many files?"
- "Does this follow our established patterns?"
- "Are we staying on plan?"

---

## Phase 1: Analysis (2-10 min)

### Project Context Check (30 seconds)

**Check for .claude/instructions.md:**
- ✅ If exists: Read and follow project guidelines, tech stack, and conventions
- ❓ If missing: Ask human for tech stack, architectural patterns, and conventions (or say 'proceed' for best practices)

### Business Objective

**Objective:** [Human provides objective here]

### Analysis Deliverables

**1. EXISTING PATTERNS SEARCH**
- Identify 2-3 existing implementations with similar patterns
- Show relevant code examples with file paths
- Document which files/classes implement related features

**2. ARCHITECTURAL CONTEXT**
- Document established layers (namespaces, interfaces)
- Identify available abstractions (base classes, interfaces, utilities)
- Map integration touch points (which methods need modification)
- Note dependency injection patterns
- Identify configuration patterns

**3. ALTERNATIVE APPROACHES**
Propose 2-3 approaches with:
- Pros and cons
- Integration complexity (low/medium/high)
- Existing code to modify vs new code to create
- Risk factors
- Estimated implementation time
- Impact on architecture

**4. RECOMMENDATION**
- Which approach and why?
- Key architectural decisions
- Patterns to follow
- Abstractions to reuse vs create
- Main integration points

**Constraints:**
- Search codebase BEFORE suggesting new patterns
- Keep analysis <500 words
- Be specific with file paths and class names
- Cite concrete code examples

**Human checkpoint:** Review analysis, provide context, approve approach before proceeding.

---

## Phase 2: Planning (2 min)

### Execution Plan

Create a detailed plan optimized for AI execution with human supervision.

**Requirements:**

1. **Numbered atomic steps** - Each completable in <15 minutes
2. **TDD discipline** - Each step starts with failing test
3. **Clear acceptance** - Observable success criteria for each step
4. **File specification** - Which files modified/created in each step
5. **Complexity tagging** - Low/Medium/High for each step
6. **Checkpoints** - Human review after every 3 steps

**Format:**

```
Step 1: [Test Description]
- Failing test: [specific test case and expected failure]
- Files: [list]
- Acceptance: [specific criteria]
- Complexity: [low/medium/high]

Step 2: [Production Code]
- Make Step 1 test pass
- Approach: [brief description]
- Files: [list]
- Acceptance: All tests pass, no regressions
- Complexity: [low/medium/high]

[Continue alternating...]

CHECKPOINTS: After steps 3, 6, 9, etc.

RISK FLAGS: [potential issues, unknowns, integration challenges]
```

**Batching:** Related tests (same class) can batch max 3 tests before going green.

**Human checkpoint:** Review granularity, verify test-first discipline, approve plan before implementation.

---

## Phase 3: Implementation (variable, <3 hours)

### TDD Execution

Execute the plan following strict TDD discipline.

**TDD Rules:**

❌ **DON'T:**
- Test interfaces (test concrete implementations)
- Use compilation errors as RED phase (use behavioral failures)
- Skip writing tests first
- Make multiple unrelated changes in one commit
- Use mocks when real components available
- Fix multiple failing tests simultaneously

✅ **DO:**
- Create stub implementations that compile but fail behaviorally
- Use real components over mocks
- Write minimum code to make test pass
- Commit after each green test (or small batch)
- Refactor after green, before next test
- Show all test output (failures and passes)

**Process for Each Step:**

**1. SHOW REASONING**
- Explain what you're about to do
- Reference specific plan step number
- Describe the failing test you'll write
- Explain why this test matters

**2. RED: Failing Test**
- Test must compile
- Test must fail behaviorally (not syntax/compilation)
- Show test code
- Run test and show failure output
- Explain what failure means

**3. GREEN: Minimal Production Code**
- Only enough to make test pass
- No premature optimization
- No "while we're here" additions
- Show production code
- Run all tests, show they pass
- Verify no regressions

**4. REFACTOR (if needed)**
- Improve code quality while tests stay green
- Remove duplication
- Improve naming and structure
- Run tests again to confirm green
- Only refactor if clear value

**5. COMMIT CHECKPOINT**
- Summarize what was accomplished
- List files changed
- Wait for human review before proceeding
- Flag any plan deviations

**Transparency:**
- Show reasoning BEFORE each step
- Explain deviations from plan
- Ask questions when context unclear
- Stop after 3 failed attempts, ask for help
- Surface integration issues immediately

**Architecture:**
- Follow patterns identified in analysis
- Use existing abstractions before creating new ones
- Match naming conventions
- Respect layer boundaries
- If pattern doesn't fit, stop and discuss

**Human supervision:** Monitor reasoning for errors, intervene when context drifts, provide missing context, redirect if off-plan, stop and replan if assumptions prove wrong.

---

## Phase 4: Completion Check (5 min)

### Verification

**1. FUNCTIONAL COMPLETENESS**
- □ All tests passing (show summary)
- □ Manual testing completed for complex features
- □ End-to-end verification if applicable
- □ No regressions in existing functionality
- □ No TODO/FIXME comments remaining
- □ All edge cases covered

**2. CODE QUALITY**
- □ Adequate test coverage
- □ Tests are meaningful (test behavior, not implementation)
- □ No duplicated code
- □ Follows established patterns
- □ Naming clear and consistent
- □ Code readable and maintainable
- □ No unnecessary complexity

**3. DOCUMENTATION**
- □ Internal code documentation accurate
- □ Complex logic has explanatory comments
- □ README updated if public API changed
- □ API documentation updated if applicable
- □ Comments explain "why", not "what"

**4. PROCESS AUDIT**
- □ Testing approach followed consistently
- □ TDD discipline maintained (test-first)
- □ No untested implementation committed
- □ Commits atomic and well-scoped
- □ All plan steps addressed or explicitly deferred
- □ Checkpoints followed

**5. ARCHITECTURAL CONSISTENCY**
- □ Respects layers and boundaries
- □ Uses existing abstractions appropriately
- □ No new patterns introduced unnecessarily
- □ Integration points clean and maintainable
- □ No circular dependencies introduced

**Narrative Summary** (2-3 paragraphs):
- What was accomplished
- How implementation went
- Notable decisions or trade-offs
- How well we followed the plan

**Outstanding Items:**
- Remaining tasks not completed
- Future improvements identified
- Technical debt created (with justification)
- Follow-up work needed

**Deviations from Plan:**
- Which steps modified or skipped
- Why deviations were necessary
- Plan calibration (too ambitious/conservative)
- Lessons for future planning

**Metrics:**
- Total commits: [#]
- Largest commit: [# lines]
- Files modified: [# files]
- Test coverage added: [estimate]
- Time spent: [hours]

**STATUS:** [Complete / Needs Work]
**READY TO CLOSE:** [Yes / No with reasoning]

**Human checkpoint:** Review checklist, spot-check claims, verify critical items, assess completeness, decide next steps.

---

## Phase 5: Retrospective (2-10 min)

### Session Learning

**1. SESSION SUMMARY**
- What accomplished?
- Time taken?
- Significant deviations?
- Assessment: [Successful / Partially successful / Struggled]

**2. CRITICAL MOMENTS**
- 2-3 moments that most impacted success/failure
- Specific decisions or interventions that were game-changers
- When human intervention proved most valuable
- Pivotal moments where we almost went wrong

**3. WASTED EFFORT**
- Wrong paths taken
- Avoidable troubleshooting
- Code duplication that existed
- Unnecessary refactorings or premature optimizations
- Time wasted [minutes]

**4. WHAT WORKED WELL**
- Most effective collaboration patterns
- Process aspects that maintained quality
- Particularly helpful prompts or instructions
- What human did well in guiding AI
- Patterns or practices to repeat

**5. WHAT COULD BE BETTER**
- What slowed us down
- Where communication broke down
- Missing context that would have helped
- Prompts needing refinement
- What would make next session smoother

**6. TECHNICAL INSIGHTS**
- Codebase learnings
- Patterns to document for team
- Refactoring opportunities for future
- Technical debt discovered
- Architectural insights

**7. PROCESS INSIGHTS**
- Did plan granularity match task complexity?
- Were steps the right size?
- Was TDD helpful or cumbersome for this task?
- Should batch sizes be adjusted?
- Were checkpoints at right frequency?
- Did analysis provide enough context?

**8. TOP IMPROVEMENT FOR NEXT SESSION**
- The ONE most valuable change for next time
- Is it prompt, process, or behavior change?
- Why will this have biggest impact?
- How specifically to implement?

Focus on what the HUMAN controls:
- Prompt language and structure changes
- Process and workflow adjustments
- How human intervenes and guides
- What context to provide proactively

**Actionable Changes** (3-5 specific):
1. [PROMPT/PROCESS/BEHAVIOR] - [Specific action]
2. [Type] - [Specific action]
3. [Type] - [Specific action]

**Knowledge Capture:**
[Document patterns, insights, or learnings to save for future reference]

**Human action:** Read fully, reflect honestly, identify top improvement, update prompts, document learnings, set intention for next session.

---

## Usage Instructions

**For a complete PDCA session:**
1. Load this file once: `Load references/fast-mode.md`
2. Provide your business objective in Phase 1
3. Work through each phase with human checkpoints
4. AI will execute all phases in sequence with your guidance

**Intervention points:**
- After Phase 1 Analysis: Review and approve approach
- After Phase 2 Planning: Review and approve plan
- During Phase 3 Implementation: Monitor every 3 steps and as needed
- After Phase 4 Completion: Verify quality claims
- After Phase 5 Retrospective: Capture learnings and improvements

**When to stop and switch to standard mode:**
- Task proving more complex than anticipated
- Need more detailed guidance at any phase
- Context drifting significantly
- First time using PDCA framework

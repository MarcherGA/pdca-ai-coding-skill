# Planning Prompt - PDCA Plan Phase

Use this prompt after completing the analysis to create a detailed execution plan with TDD steps.

## When to Use

- After analysis is complete and approach is approved
- When you need to break down the work into testable increments
- Before starting any code implementation

## Planning Prompt

```
PLANNING PHASE - Execution Plan

Based on our analysis, provide a coherent plan incorporating our refinements that is optimized for YOUR use as context for the implementation.

This plan is FOR YOU (the AI agent) to follow during implementation. Make it detailed enough that you can execute it step-by-step while maintaining context and coherence.

EXECUTION CONTEXT:
- This plan will be implemented step-by-step following TDD discipline
- Each step must have clear stop/go criteria
- Implementation will occur in the same context thread
- Human will supervise and intervene as needed

PLAN REQUIREMENTS:

1. Break work into numbered, atomic steps
2. Each step must:
   - Be completable in <15 minutes
   - Have a specific failing test as the starting point
   - Include explicit acceptance criteria
   - Specify which files will be modified/created
   - Note estimated complexity (low/medium/high)

3. TDD DISCIPLINE:
   - Each step MUST start with a failing test
   - Limit to 3 attempts before stopping to ask for help
   - Production code only after test is red (behaviorally failing)
   - No compilation errors as "red" - tests must compile but fail behaviorally

4. MODEL SELECTION (optional):
   - Tag each step with complexity: [SIMPLE/MODERATE/COMPLEX]
   - Simple steps may use lighter models
   - Complex steps requiring reasoning use more capable models
   - Human can adjust model selection during execution

5. PROCESS CHECKPOINTS:
   - After every 3 steps, pause for human review
   - Flag any deviations from established patterns
   - Highlight when manual testing or end-to-end verification is needed

FORMAT:

Step 1: [Test Description]
- Failing test: [specific test case and expected failure]
- Files to modify: [list specific files]
- Acceptance: [specific criteria - what makes this step complete]
- Estimated complexity: [low/medium/high]

Step 2: [Production Code]
- Make Step 1 test pass
- Implementation approach: [brief description]
- Files to modify: [list]
- Acceptance: All tests pass, no regressions
- Estimated complexity: [low/medium/high]

[Continue alternating test/code for all steps...]

CHECKPOINT SCHEDULE:
- Human review after steps: 3, 6, 9, etc.
- Final verification after all steps complete

BATCHING GUIDELINES:
- Related tests (same class/feature) can be batched
- Maximum 3 tests per batch before going green
- Each batch = one commit

RISK FLAGS:
- [List any potential issues, unknowns, or integration challenges]
- [Note any steps that might need extra attention]
- [Identify dependencies on external systems or APIs]
```

## Expected Output

The AI should provide:

1. **Numbered Steps** - Clear sequence of test → code pairs
2. **Specific Tests** - Exact test cases, not vague descriptions
3. **File Paths** - Which files will be touched in each step
4. **Acceptance Criteria** - Observable success conditions
5. **Checkpoints** - Clear review points every 3 steps
6. **Risk Flags** - Known challenges or unknowns

## Human Follow-Up Actions

After receiving the plan:

1. ✅ **Review step granularity** - Are steps small enough?
2. ✅ **Check test-first discipline** - Every odd step a test?
3. ✅ **Verify file organization** - Are we touching the right files?
4. ✅ **Assess risk flags** - Do we need to address any before starting?
5. ✅ **Approve plan** - Explicitly approve before implementation

## Red Flags to Watch For

- ⚠️ Steps that don't start with failing tests
- ⚠️ Steps that seem too large (>15 min)
- ⚠️ Vague acceptance criteria ("make it work")
- ⚠️ No checkpoints defined
- ⚠️ Missing risk assessment

If you see these, ask the AI to refine the plan.

## Example Usage

```
Human: Load references/planning-prompt.md and create the execution plan

AI: [Provides 12 numbered steps alternating between writing tests 
and implementing code, with checkpoints at steps 3, 6, 9, and 12]
```

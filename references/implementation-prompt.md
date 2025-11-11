# Implementation Prompt - PDCA Do Phase

Use this prompt to execute the plan following strict TDD discipline.

## Working Agreements (Quick Reference)

**Core Principles:**
- ✅ **Test-First**: Failing tests before production code (behavioral failures, not compilation errors)
- ✅ **Small Commits**: <100 lines, <5 files, one logical change
- ✅ **Follow Patterns**: Search and reuse existing abstractions
- ✅ **You Own It**: Review AI reasoning, intervene early, commit only what you understand

**Key Interventions:** "Where's the failing test first?" • "Is this commit too large?" • "Does this follow our patterns?" • "Are we staying on plan?"

## When to Use

- After the plan is approved and ready to implement
- At the start of the Do phase of PDCA cycle

## Implementation Prompt

```
IMPLEMENTATION PHASE - Test-Driven Development

Execute the plan we created, following TDD discipline strictly.

TDD RULES:

❌ DON'T:
- Test interfaces - test concrete implementations
- Use compilation errors as RED phase - use behavioral failures
- Skip writing tests first
- Make multiple unrelated changes in one commit
- Use mocks when real components are available
- Fix multiple failing tests simultaneously

✅ DO:
- Create stub implementations that compile but fail behaviorally
- Use real components over mocks when possible
- Write the minimum code to make the test pass
- Commit after each green test (or small batch of related tests)
- Refactor after green, before moving to next test
- Show all test output (both failures and passes)

PROCESS FOR EACH STEP:

1. SHOW YOUR REASONING
   - Explain what you're about to do
   - Reference the specific plan step number
   - Describe the failing test you'll write
   - Explain why this test matters

2. RED: Write the failing test
   - Test must compile
   - Test must fail for behavioral reasons (not syntax/compilation)
   - Show me the test code
   - Run the test and show me the failure output
   - Explain what the failure means

3. GREEN: Write minimal production code
   - Only enough code to make the test pass
   - No premature optimization
   - No "while we're here" additions
   - Show me the production code
   - Run all tests and show me they pass
   - Verify no regressions in other tests

4. REFACTOR (if needed)
   - Improve code quality while keeping tests green
   - Remove duplication
   - Improve naming and structure
   - Run tests again to confirm still green
   - Only refactor if there's clear value

5. COMMIT CHECKPOINT
   - Summarize what was accomplished
   - List files changed
   - Wait for human review before proceeding
   - Flag any deviations from plan

BATCHING RULES:
- Related tests (same class/feature) can be batched
- Maximum 3 tests per batch before going green
- All tests in batch must pass before moving forward
- Each batch = one coherent commit
- Document the batch scope upfront

TRANSPARENCY REQUIREMENTS:
- Show your reasoning BEFORE each step
- Explain any deviations from the plan
- Ask questions when context is unclear or assumptions needed
- Stop after 3 failed attempts and ask for help
- Surface any integration issues immediately

ARCHITECTURAL CONSISTENCY:
- Follow the patterns identified in analysis
- Use existing abstractions before creating new ones
- Match naming conventions from codebase
- Respect layer boundaries and separation of concerns
- If pattern doesn't fit, stop and discuss with human

ERROR HANDLING:
- If a test fails unexpectedly, stop and analyze why
- If multiple tests fail, fix them one at a time
- If you're unsure about an approach, ask before implementing
- If regression tests fail, stop immediately and investigate

Proceed with Step 1 of the plan. Show your reasoning first.
```

## Expected Behavior

The AI should:

1. **Explain before acting** - Clear reasoning for each step
2. **Show all output** - Test failures and passes
3. **Follow red-green-refactor** - Strict TDD discipline
4. **Commit frequently** - After each successful step/batch
5. **Ask when uncertain** - Don't make blind assumptions
6. **Stop on failures** - Investigate, don't push through

## Human Actions During Implementation

**Monitor for:**
- Reasoning errors (catch early!)
- Context drift (AI going off-pattern)
- Skipped tests
- Too much code at once
- Assumptions without verification

**Intervene when:**
- AI skips tests: "Stop. Write the failing test first."
- Changes too big: "This is too much at once. Break it down."
- Context drifts: "Return to step X. Follow the [pattern] we identified."
- Wrong assumptions: "That's not correct. The actual pattern is [X]."
- Stuck in a loop: "Let's stop and replan from where we are."

## Red Flags to Watch For

- ⚠️ No test failures shown
- ⚠️ Implementing without tests
- ⚠️ Making unrelated changes
- ⚠️ Creating new patterns instead of using existing
- ⚠️ Large commits (>100 lines)
- ⚠️ Touching many files at once

## Example Interaction

```
Human: Load references/implementation-prompt.md and execute the plan

AI: Starting with Step 1: Create failing test for JWT token generation

REASONING: We need to verify that JWTService can generate a valid token
with user claims. This test will fail because JWTService doesn't exist yet.

RED PHASE:
[Shows test code]
[Runs test, shows failure: "JWTService not defined"]

Wait - this is a compilation error, not a behavioral failure. Let me create
the stub first.

[Creates JWTService stub with generate_token() returning None]
[Runs test again]
[Shows failure: "Expected token string, got None"]

Now we have a proper behavioral failure.

GREEN PHASE:
[Implements minimal JWT generation]
[Runs all tests]
[Shows all tests pass]

Ready to commit. Files changed: JWTService.py, test_jwt_service.py
Proceeding to Step 2? [Waits for human approval]
```

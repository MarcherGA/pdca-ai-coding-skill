# Completion Check Prompt - PDCA Check Phase

Use this prompt after implementation to verify quality and completeness.

## When to Use

- After all implementation steps are complete
- Before considering the work "done"
- As input for code review

## Completion Check Prompt

```
COMPLETENESS CHECK - Session Review

Review our original goal and plan against our execution.

VERIFICATION CHECKLIST:

1. FUNCTIONAL COMPLETENESS
   □ All tests passing (show test summary)
   □ Manual testing completed for complex features
   □ End-to-end verification done if applicable
   □ No regressions introduced in existing functionality
   □ No TODO/FIXME comments remaining created by this test driving session
   □ All edge cases covered by tests

2. CODE QUALITY
   □ Production code has adequate test coverage
   □ Tests are meaningful and test behavior (not implementation)
   □ No duplicated code blocks
   □ Follows established patterns from codebase
   □ Naming is clear and consistent with project conventions
   □ Code is readable and maintainable
   □ No unnecessary complexity

3. DOCUMENTATION
   □ Internal code documentation is accurate
   □ Complex logic has explanatory comments
   □ README updated if public API changed
   □ API documentation updated if applicable
   □ Comments explain "why", not "what"

4. PROCESS AUDIT
   □ Testing approach was followed consistently
   □ TDD discipline maintained (test-first)
   □ No untested implementation was committed
   □ Commits are atomic and well-scoped
   □ All plan steps were addressed or explicitly deferred
   □ Checkpoints were followed

5. ARCHITECTURAL CONSISTENCY
   □ Respects established layers and boundaries
   □ Uses existing abstractions appropriately
   □ Doesn't introduce new patterns unnecessarily
   □ Integration points are clean and maintainable
   □ No circular dependencies introduced

NARRATIVE SUMMARY:
[Provide 2-3 paragraph summary covering:
- What was accomplished
- How the implementation went
- Any notable decisions or trade-offs made
- How well we followed the plan]

OUTSTANDING ITEMS:
[List any:
- Remaining tasks not completed
- Future improvements identified
- Technical debt created (with justification)
- Follow-up work needed]

DEVIATIONS FROM PLAN:
[Explain:
- Which steps were modified or skipped
- Why deviations were necessary
- Whether plan was too ambitious/conservative
- Lessons for future planning]

METRICS SUMMARY:
- Total commits: [#]
- Largest commit size: [# lines]
- Files modified: [# files]
- Test coverage added: [estimate if known]
- Time spent: [hours]

STATUS: [Complete / Needs Work]

READY TO CLOSE: [Yes / No with reasoning]

If "Needs Work":
- Specify exactly what remains
- Estimate effort required
- Note any blockers or dependencies
```

## Expected Output

The AI should provide:

1. **Checklist** - All items marked complete or flagged
2. **Narrative** - 2-3 paragraphs explaining what happened
3. **Outstanding Items** - Clear list of remaining work
4. **Deviations** - Honest assessment of plan adherence
5. **Status** - Clear yes/no on readiness

## Human Actions After Completion Check

1. ✅ **Review checklist** - Spot-check AI claims
2. ✅ **Verify critical items** - Run tests yourself
3. ✅ **Check code quality** - Quick code review
4. ✅ **Assess completeness** - Is it really done?
5. ✅ **Save completion analysis** - Add to project tracking
6. ✅ **Decide next steps** - Close or continue?

## Red Flags to Watch For

- ⚠️ Many checklist items not checked
- ⚠️ Vague narrative ("everything went fine")
- ⚠️ No deviations acknowledged (probably not honest)
- ⚠️ Large outstanding items list
- ⚠️ "Ready to close: Yes" with unchecked items

If you see these, dig deeper before closing.

## Example Usage

```
Human: Load references/completion-prompt.md and verify our work

AI: 
COMPLETENESS CHECK

VERIFICATION CHECKLIST:
✓ All tests passing (47 tests, 0 failures)
✓ Manual testing completed (JWT auth tested via Postman)
✓ No regressions (all existing auth tests still pass)
✓ No TODO comments remaining
✓ Test coverage adequate (new code 95% covered)
✓ No duplicated code
✓ Follows existing auth patterns
... [continues through all items]

NARRATIVE SUMMARY:
Successfully implemented JWT authentication with refresh tokens
following the established auth patterns in AuthService. Implementation
went smoothly with only minor deviations from plan...

STATUS: Complete
READY TO CLOSE: Yes - all acceptance criteria met
```

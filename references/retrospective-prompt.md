# Retrospective Prompt - PDCA Act Phase

Use this prompt at the end of every session to learn and improve.

## Working Agreements (Quick Reference)

**Core Principles:**
- ✅ **Test-First**: Failing tests before production code (behavioral failures, not compilation errors)
- ✅ **Small Commits**: <100 lines, <5 files, one logical change
- ✅ **Follow Patterns**: Search and reuse existing abstractions
- ✅ **You Own It**: Review AI reasoning, intervene early, commit only what you understand

**Key Interventions:** "Where's the failing test first?" • "Is this commit too large?" • "Does this follow our patterns?" • "Are we staying on plan?"

## When to Use

- After completion check is done
- Before closing the session
- To capture learnings for next time

## Retrospective Prompt

```
RETROSPECTIVE - Session Learning and Improvement

Analyze our collaboration session to identify improvements for future work.

1. SESSION SUMMARY
   - What did we accomplish?
   - How long did it take (estimated)?
   - Were there significant deviations from the plan?
   - Overall assessment: [Successful / Partially successful / Struggled]

2. CRITICAL MOMENTS ANALYSIS
   - What were the 2-3 moments where our approach most impacted success/failure?
   - What specific decisions or interventions were game-changers?
   - When did human intervention prove most valuable?
   - Were there pivotal moments where we almost went wrong?

3. WASTED EFFORT
   - Were there any wrong paths we went down?
   - What troubleshooting could have been avoided?
   - Did we duplicate any code that already existed?
   - Were there unnecessary refactorings or premature optimizations?
   - How much time was wasted? [estimate in minutes]

4. WHAT WORKED WELL
   - Which collaboration patterns were most effective?
   - What aspects of our process helped maintain quality?
   - Which prompts or instructions were particularly helpful?
   - What did the human do well in guiding the AI?
   - What patterns or practices should we repeat?

5. WHAT COULD BE BETTER
   - What slowed us down?
   - Where did communication break down?
   - What context was missing that would have helped?
   - Which prompts need refinement?
   - What would make the next session smoother?

6. TECHNICAL INSIGHTS
   - What did we learn about the codebase?
   - Are there patterns we should document for the team?
   - Are there refactoring opportunities for future work?
   - Did we discover any technical debt?
   - Any architectural insights to share?

7. PROCESS INSIGHTS
   - Did the plan granularity match the task complexity?
   - Were steps the right size?
   - Was TDD discipline helpful or cumbersome for this task?
   - Should we adjust batch sizes for similar work?
   - Were checkpoints at the right frequency?
   - Did analysis phase provide enough context?

8. PROMPT REFINEMENT NEEDS
   - Analysis prompt: [Any changes needed?]
   - Planning prompt: [Any changes needed?]
   - Implementation prompt: [Any changes needed?]
   - Completion prompt: [Any changes needed?]
   - Retrospective prompt: [Any changes needed?]

9. TOP IMPROVEMENT FOR NEXT SESSION
   - What is the ONE most valuable change I should make next time?
   - Is it a prompt change, process change, or human behavior change?
   - Why will this have the biggest impact?
   - How specifically should it be implemented?

IMPORTANT: Focus on what the HUMAN can control and change:
- Changes to prompt language and structure
- Adjustments to process and workflow  
- Changes in how the human intervenes and guides
- What context to provide proactively
These are the only levers the human controls to improve results.

ACTIONABLE CHANGES:
[List 3-5 specific, concrete changes to make for the next session]

1. [Change type: PROMPT/PROCESS/BEHAVIOR] - [Specific action]
2. [Change type] - [Specific action]
3. [Change type] - [Specific action]

KNOWLEDGE CAPTURE:
[Document any patterns, insights, or learnings that should be saved for future reference]
```

## Expected Output

The AI should provide:

1. **Honest assessment** - Both successes and failures
2. **Specific moments** - Not vague generalizations
3. **Concrete insights** - Actionable observations
4. **Clear top improvement** - One focused change
5. **Actionable changes** - 3-5 specific next steps

## Human Actions After Retrospective

1. ✅ **Read fully** - Don't skip this step!
2. ✅ **Reflect honestly** - Do you agree with assessment?
3. ✅ **Identify top improvement** - Focus on one thing
4. ✅ **Update prompts** - Make changes right away
5. ✅ **Document learnings** - Save in knowledge base
6. ✅ **Set intention** - Commit to improvement for next time

## Using Retrospective Data

**Track over time:**
- Common pain points across sessions
- Patterns in what works well
- Evolution of prompt effectiveness
- Types of interventions needed

**Update your PDCA practice:**
- Refine prompt templates
- Adjust working agreements
- Calibrate planning granularity
- Improve intervention strategies

**Share with team:**
- Codebase patterns discovered
- Effective AI collaboration techniques
- Process improvements that work
- Architectural insights

## Red Flags to Watch For

- ⚠️ "Everything went perfectly" (not realistic)
- ⚠️ No specific improvements identified
- ⚠️ Blaming AI without self-reflection
- ⚠️ Vague, non-actionable changes
- ⚠️ Skipping the retrospective entirely

The retrospective is WHERE IMPROVEMENT HAPPENS. Don't skip it!

## Example Usage

```
Human: Load references/retrospective-prompt.md and analyze our session

AI:
RETROSPECTIVE

1. SESSION SUMMARY
Accomplished: Full JWT authentication with refresh tokens
Time: ~2.5 hours
Deviations: Added token blacklist (not in original plan)
Assessment: Successful

2. CRITICAL MOMENTS
- Human caught me about to skip test for token expiration check
- Decision to use existing Redis cache for blacklist saved time
- Intervention when I started creating new base classes instead of using existing

3. WASTED EFFORT
- Spent 20 minutes on premature optimization of token generation
- Initially missed existing TokenCache abstraction
- 15 minutes debugging because I tested the interface instead of implementation

... [continues through all sections]

9. TOP IMPROVEMENT FOR NEXT SESSION
CHANGE TYPE: PROCESS
Spend 5 more minutes in analysis phase explicitly searching for 
ALL abstractions, not just similar features. This would have caught
TokenCache immediately and saved 15 minutes of implementation time.

ACTIONABLE CHANGES:
1. [PROMPT] Add "list ALL available abstractions" to analysis prompt
2. [BEHAVIOR] Human should verify abstraction search before approving plan
3. [PROCESS] Add "existing abstractions check" to step 1 of planning
```

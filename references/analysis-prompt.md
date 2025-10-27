# Analysis Prompt - PDCA Plan Phase

Use this prompt at the start of each coding session to analyze the business problem and identify the best technical approach.

## When to Use

- At the beginning of every feature implementation
- When refactoring or adding cross-system functionality
- Before making significant architectural changes
- Any time you need to understand existing patterns before coding

## Analysis Prompt

```
ANALYSIS PHASE - Business Problem and Technical Approach

Business Objective:
[The human will fill this in - what are they trying to achieve and why?]

Required Deliverables BEFORE Analysis:

1. EXISTING PATTERNS SEARCH
   - Identify 2-3 existing implementations that follow similar patterns
   - Search the codebase for comparable functionality
   - Document which files/classes implement related features
   - Show relevant code examples from the codebase

2. ARCHITECTURAL CONTEXT
   - Document the established architectural layers (which namespaces, which interfaces)
   - Identify the abstractions already available (base classes, interfaces, utilities)
   - Map integration touch points (which existing methods will need modification)
   - Note the dependency injection patterns used
   - Identify where similar features are configured

3. CONFIGURATION & SETUP
   - Identify where similar features are configured
   - Document configuration file patterns used in the project
   - Note any environment-specific considerations
   - Check for feature flags or settings that may be relevant

4. ALTERNATIVE APPROACHES
   - Propose 2-3 different technical approaches to solve this problem
   - For each approach, provide:
     * Pros and cons
     * Integration complexity (low/medium/high)
     * Amount of existing code to modify vs create new
     * Risk factors
     * Estimated implementation time
     * Impact on existing architecture

5. RECOMMENDED APPROACH
   - Which approach do you recommend and why?
   - What are the key architectural decisions?
   - What existing patterns should we follow?
   - What abstractions should we reuse vs create?
   - What are the main integration points?

CONSTRAINTS:
- Focus on "what" and "why", not implementation details
- Search the codebase BEFORE suggesting new code patterns
- Keep analysis human-readable and under 500 words
- Identify code reuse opportunities - avoid duplication
- Be specific with file paths and class names
- Cite specific code examples when describing patterns

OUTPUT FORMAT:
Provide a clear, structured analysis that addresses all 5 deliverables above.
Use markdown formatting for readability.
This analysis will be added to project tracking (Jira/Linear), so make it clear and professional.
```

## Expected Output

The AI should provide:

1. **Existing Patterns** - 2-3 concrete examples with file paths
2. **Architecture** - Clear description of layers, abstractions, DI patterns
3. **Configuration** - Where and how this feature should be configured
4. **Alternatives** - 2-3 approaches with detailed pros/cons
5. **Recommendation** - Clear recommendation with justification

## Human Follow-Up Actions

After receiving the analysis:

1. ✅ **Review thoroughly** - Check that patterns cited actually exist
2. ✅ **Ask clarifying questions** - If anything is unclear or missing
3. ✅ **Provide additional context** - Share domain knowledge the AI lacks
4. ✅ **Approve approach** - Explicitly approve before moving to planning
5. ✅ **Save to project tracker** - Document in Jira/Linear for transparency

## Red Flags to Watch For

- ⚠️ No existing patterns cited (may duplicate code)
- ⚠️ Vague architectural descriptions
- ⚠️ Only one approach proposed
- ⚠️ No consideration of integration points
- ⚠️ Recommendation lacks clear justification

If you see these, ask the AI to dig deeper before proceeding.

## Example Usage

```
Human: Load references/analysis-prompt.md and analyze: 
Add user authentication with JWT tokens to our REST API

AI: [Provides detailed analysis searching for existing auth patterns, 
documenting API layers, proposing JWT vs OAuth vs session approaches, 
recommending JWT with refresh tokens based on existing patterns]
```

# Project-Specific Configuration Guide

## Overview

The PDCA skill works **globally** across all your projects, but you can add **project-specific configuration** to customize behavior for individual codebases.

This is optional but recommended for:
- Complex projects with specific conventions
- Team projects requiring consistency
- Projects using uncommon tech stacks or patterns
- When you find yourself repeating the same context every session

---

## Two-Layer Architecture

```
┌────────────────────────────────────────┐
│  PDCA Skill (Global)                   │  ← Installed once in Claude.ai
│  "Process: How to approach any task"   │     Provides the workflow framework
└────────────────────────────────────────┘
                 ↓ applies to
┌────────────────────────────────────────┐
│  .claude/instructions.md (Per-Project) │  ← Optional, in project root
│  "Context: What this project uses"     │     Provides project specifics
└────────────────────────────────────────┘
```

**They work together:**
- PDCA skill = Process (Plan-Do-Check-Act workflow)
- Project config = Context (this project's tech stack and rules)

---

## Creating `.claude/instructions.md`

### When to Create One

**Create a project config file when:**
- ✅ You have specific tech stack choices (Next.js vs React, TypeScript vs JavaScript)
- ✅ You follow specific architectural patterns (Clean Architecture, DDD, etc.)
- ✅ You have team conventions that differ from defaults
- ✅ You use uncommon or custom frameworks
- ✅ You keep forgetting to mention project details each session

**Skip it when:**
- ❌ Simple personal projects with standard tech
- ❌ You're just prototyping or experimenting
- ❌ You use common defaults (Create React App, Express, etc.)

### How to Create

1. **Navigate to your project root:**
   ```bash
   cd /path/to/your/project
   ```

2. **Create `.claude` directory:**
   ```bash
   mkdir .claude
   ```

3. **Create `instructions.md` file:**
   ```bash
   touch .claude/instructions.md
   ```

4. **Add your project context** (see template below)

5. **Commit to git** (so team members get it too):
   ```bash
   git add .claude/instructions.md
   git commit -m "Add Claude project configuration"
   ```

---

## Template: Minimal Configuration

Use this for most projects (keep it under 100 lines):

```markdown
# Project Configuration for Claude

## Tech Stack
- **Framework:** [e.g., Next.js 14 with App Router]
- **Language:** [e.g., TypeScript (strict mode)]
- **Database:** [e.g., PostgreSQL with Prisma ORM]
- **Styling:** [e.g., Tailwind CSS]
- **Testing:** [e.g., Jest + React Testing Library]
- **Deployment:** [e.g., Vercel]

## Architecture Patterns
- [e.g., Server Components by default]
- [e.g., Client components only when needed - mark with 'use client']
- [e.g., API routes in app/api/]
- [e.g., Database queries in server components or server actions]

## Project Conventions
1. [e.g., Use functional components exclusively]
2. [e.g., One component per file]
3. [e.g., Name files with kebab-case: user-profile.tsx]
4. [e.g., Put shared utilities in lib/]
5. [e.g., Put components in components/]

## Important Constraints
- [e.g., Must support Safari 14+]
- [e.g., Keep bundle size under 200KB]
- [e.g., All forms must have CSRF protection]

## Custom Code Patterns
- **Authentication:** [e.g., Use NextAuth.js with JWT strategy]
- **Error Handling:** [e.g., Use custom error boundary in app/error.tsx]
- **Logging:** [e.g., Use Winston logger in lib/logger.ts]
- **API Responses:** [e.g., Always return {success: boolean, data?: any, error?: string}]

## Don't Do
- ❌ [e.g., Don't use class components]
- ❌ [e.g., Don't install new dependencies without approval]
- ❌ [e.g., Don't bypass our auth middleware]
```

---

## Template: Comprehensive Configuration

Use this for complex enterprise projects:

```markdown
# Project Configuration for Claude

## Project Overview
**Name:** [Project name]
**Description:** [1-2 sentence description]
**Team Size:** [e.g., 5 developers]
**Stage:** [e.g., Production, Beta, MVP]

## Tech Stack
### Frontend
- Framework: [e.g., Next.js 14]
- Language: [e.g., TypeScript 5.2 (strict)]
- State: [e.g., Zustand]
- Forms: [e.g., React Hook Form + Zod]
- Styling: [e.g., Tailwind CSS + CVA]
- Testing: [e.g., Vitest + Testing Library]

### Backend
- Runtime: [e.g., Node.js 20]
- Framework: [e.g., tRPC]
- Database: [e.g., PostgreSQL 16]
- ORM: [e.g., Prisma 5]
- Cache: [e.g., Redis]
- Queue: [e.g., Bull]

### Infrastructure
- Hosting: [e.g., AWS ECS]
- CI/CD: [e.g., GitHub Actions]
- Monitoring: [e.g., Datadog]

## Architecture

### Folder Structure
```
src/
├── app/              # Next.js app router pages
├── components/       # React components
│   ├── ui/          # shadcn/ui components
│   └── features/    # Feature-specific components
├── lib/             # Shared utilities
├── server/          # Backend code
│   ├── api/        # tRPC routers
│   ├── db/         # Database access layer
│   └── services/   # Business logic
└── types/           # TypeScript types
```

### Design Patterns
1. **Component Pattern:** [e.g., Compound components for complex UI]
2. **Data Fetching:** [e.g., Server components with React Query for client]
3. **Error Handling:** [e.g., Error boundaries + toast notifications]
4. **Auth:** [e.g., Custom JWT middleware + refresh tokens]

## Coding Standards

### Naming Conventions
- Components: PascalCase (UserProfile.tsx)
- Files: kebab-case (user-profile.utils.ts)
- Functions: camelCase (getUserById)
- Constants: SCREAMING_SNAKE_CASE (API_BASE_URL)
- Types/Interfaces: PascalCase with descriptive names

### Code Organization
- One component per file
- Colocate tests with source files (.test.ts)
- Group related files in feature folders
- Keep files under 200 lines (split if larger)
- Export types separately from implementation

### TypeScript Rules
- No `any` types (use `unknown` if needed)
- Prefer interfaces over types for objects
- Use discriminated unions for complex states
- Explicit return types for public functions

## Testing Requirements
- **Unit Tests:** All utilities and hooks
- **Integration Tests:** All API endpoints
- **E2E Tests:** Critical user flows
- **Coverage Target:** 80% overall, 100% for critical paths
- **Test Naming:** describe("[Component/Function]", () => { it("should [behavior]", ...)})

## Performance Constraints
- **Bundle Size:** < 300KB (measured at build)
- **First Paint:** < 1.5s
- **Time to Interactive:** < 3s
- **API Latency:** < 200ms (p95)

## Security Requirements
- All user inputs must be validated (Zod schemas)
- All API routes must check authentication
- SQL queries must use parameterized statements
- Secrets must use environment variables (never commit)
- CSRF tokens required for state-changing operations

## Custom Patterns & Utilities

### API Responses
Always use standard response format:
```typescript
type ApiResponse<T> = {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: any;
  };
};
```

### Error Handling
Use custom error classes in `lib/errors.ts`:
- `ValidationError` - User input errors
- `AuthenticationError` - Auth failures
- `AuthorizationError` - Permission denied
- `NotFoundError` - Resource not found

### Database Access
Always use repository pattern from `server/db/repositories/`:
```typescript
// ✅ Good
const user = await userRepository.findById(id);

// ❌ Bad - Don't query Prisma directly
const user = await prisma.user.findUnique({where: {id}});
```

## Dependencies
### Must Use
- [e.g., Use date-fns (not moment.js)]
- [e.g., Use zod for validation]
- [e.g., Use Winston for logging]

### Don't Use
- ❌ [e.g., lodash - use native JS methods]
- ❌ [e.g., axios - use native fetch]
- ❌ [e.g., moment.js - deprecated]

## Deployment & CI/CD
- **Branch Strategy:** GitFlow (main, develop, feature branches)
- **PR Requirements:** 2 approvals, all checks passing, up-to-date with target
- **Commit Messages:** Follow Conventional Commits
- **Deployment:** Automatic on merge to main (after CI passes)

## Team Practices
- Code reviews within 24 hours
- Update tests when changing functionality
- Document complex logic with comments
- Update README for setup changes
- Pair programming for complex features

## Important Links
- [Design System](...)
- [API Documentation](...)
- [Architecture Decision Records](...)
- [Runbook](...)
```

---

## How It Works in Practice

### Example: Without Project Config

```
You: "Let's implement user authentication"

Claude: "I'll analyze approaches... 
Should we use NextAuth, Passport, or custom JWT?"

You: "We use NextAuth"

Claude: "Got it. Should I use sessions or JWT?"

You: "JWT with refresh tokens, store in PostgreSQL"

Claude: "Understood. Where should I put the configuration?"

You: "In lib/auth.ts, follow our existing pattern"
```
**Problem:** You waste time repeating context every session!

### Example: With Project Config

```
You: "Let's implement user authentication"

Claude: "I see this is a Next.js project using NextAuth with JWT.
I'll implement authentication following your existing pattern
in lib/auth.ts with PostgreSQL for refresh tokens.

Let me analyze similar auth patterns in your codebase..."
```
**Result:** Claude already knows your stack and patterns!

---

## Best Practices

### Keep It Concise
- ✅ DO: Document deviations from common practices
- ✅ DO: Link to external docs instead of duplicating
- ❌ DON'T: Document obvious things
- ❌ DON'T: Duplicate what's in the PDCA skill

### Update It
- Review quarterly or after major architecture changes
- Update when new conventions are established
- Remove outdated patterns
- Keep it living documentation

### Version Control
- Commit `.claude/instructions.md` to git
- Include in code reviews
- Update in feature branches that change architecture
- Treat it like code documentation

---

## FAQ

**Q: Do I need this for every project?**
A: No! Only for projects where you have specific conventions or keep repeating the same context.

**Q: Can I have multiple instruction files?**
A: Claude Code reads `.claude/instructions.md` at the project root. You can have different files per project.

**Q: What if my project uses multiple languages/frameworks?**
A: Document all of them! E.g., "Frontend: React, Backend: Python FastAPI, Mobile: React Native"

**Q: How does this interact with the PDCA skill?**
A: Perfectly! The PDCA skill provides the process, your config provides the context. See "Two-Layer Architecture" above.

**Q: Can I use this without the PDCA skill?**
A: Yes! `.claude/instructions.md` works independently. But combining both gives you process + context.

**Q: My team doesn't use Claude Code, is this still useful?**
A: The concept yes, but `.claude/instructions.md` is specific to Claude Code CLI. For other tools, you'll need to provide context manually each session.

---

## Examples from Real Projects

### Example 1: E-commerce Platform
```markdown
# E-commerce Platform - Claude Config

## Stack
- Next.js 14, TypeScript, Tailwind, Prisma, PostgreSQL
- Stripe for payments, SendGrid for emails

## Key Patterns
- All products have variants (never single products)
- Prices include tax (display logic in lib/pricing.ts)
- Cart stored in Redis (session in PostgreSQL)
- Inventory updates via queue (lib/queue/inventory.ts)

## Don't Do
- Don't bypass inventory checks
- Don't process payments without 3D Secure
- Don't send emails synchronously (use queue)
```

### Example 2: Internal Dashboard
```markdown
# Admin Dashboard - Claude Config

## Stack
- React 18, TypeScript, Recharts, TanStack Query, Express API

## Important
- All data is sensitive - log access in audit_log table
- Multi-tenant: always filter by tenantId from auth token
- Charts must support date range filters
- Dark mode only (design requirement)

## Auth
- JWT from /api/auth/login
- Refresh token stored in httpOnly cookie
- Check permissions with hasPermission() in lib/auth.ts
```

### Example 3: Mobile App Backend
```markdown
# Mobile API - Claude Config

## Stack
- Node.js, Express, MongoDB, Redis, AWS S3

## Mobile-Specific
- API versioning: /v1/, /v2/ (support last 2 versions)
- All responses include appVersion field
- Push notifications via FCM (lib/notifications.ts)
- Images must generate thumbnails (lib/images.ts)
- Offline support: include syncToken in responses

## Performance
- All list endpoints must paginate (max 100 items)
- Cache frequently accessed data in Redis (5min TTL)
- Lazy load images (return URLs, not base64)
```

---

## Summary

**TL;DR:**
1. PDCA skill = Global process framework (install once)
2. `.claude/instructions.md` = Per-project context (optional)
3. Together = Best results (consistent process + project knowledge)
4. Only create `.claude/instructions.md` for projects with specific needs
5. Keep it under 100 lines for maintainability

**When in doubt:** Start without project config, add it when you find yourself repeating context!

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-27

### Added
- Dedicated working-agreements.md reference file with comprehensive detail
- Model selection tagging in planning prompt for cost optimization
- Explicit "plan for AI use" emphasis in planning phase
- Artifact creation notes for Jira/Linear integration
- Human control focus in retrospective (what developer can change)
- CONTRIBUTING.md with community guidelines
- GitHub issue and PR templates
- Comprehensive documentation structure

### Changed
- SKILL.md now leaner, points to detailed references
- Planning prompt emphasizes plan is for AI agent's use during implementation
- Completion check specifies "TODO from THIS test driving session"
- Retrospective clarifies focus on human-controllable improvements
- Improved batching strategy explanation
- Enhanced transparency requirements throughout

### Fixed
- Aligned all prompts precisely with InfoQ article intent
- Clarified when to use different complexity variations
- Improved intervention point descriptions

## [1.0.0] - 2025-10-26

### Added
- Initial release of PDCA AI Coding Skill
- 5-phase PDCA workflow (Analysis, Planning, Implementation, Check, Retrospective)
- Test-driven development discipline with batching
- Quality metrics tracking script (track_metrics.py)
- Session initialization script (init_session.py)
- Session logging template
- Complete prompt templates for all phases
- Working agreements for human accountability
- Documentation and quick start guides

### Core Features
- Structured prompting for AI code generation
- Red-green-refactor TDD cycle
- Codebase pattern analysis
- Atomic commit encouragement
- Continuous improvement through retrospectives
- Context drift detection
- Human intervention guidelines

---

## Future Roadmap

### Planned for 1.2.0
- [ ] Framework-specific adaptations (React, Django, FastAPI)
- [ ] Language-specific prompt variations
- [ ] GitHub Actions for automated metrics
- [ ] Extended examples and case studies
- [ ] Video tutorial for workflow

### Under Consideration
- [ ] Integration with VS Code extension
- [ ] Advanced metrics dashboard
- [ ] Team collaboration features
- [ ] Alternative workflow templates
- [ ] Multi-language support

---

**Legend:**
- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Vulnerability fixes

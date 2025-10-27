# Security Policy

## Supported Versions

Currently supported versions of the PDCA AI Coding Skill:

| Version | Supported          |
| ------- | ------------------ |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Security Considerations

### Scripts
The Python scripts in this repository:
- Do not connect to external services (except git repositories you specify)
- Do not transmit data outside your local environment
- Only read/write files in directories you specify
- Are designed to be reviewed before use

### Skill File
The `.skill` file:
- Contains only prompts and instructions
- Does not execute code automatically
- Requires Claude.ai upload (follows their security model)
- Is a ZIP archive you can inspect

### Best Practices When Using This Skill

1. **Review Generated Code**: Always review AI-generated code before committing
2. **Sensitive Data**: Don't include API keys, credentials, or sensitive data in prompts
3. **Access Control**: Keep your coding sessions and logs private
4. **Dependencies**: Review all dependencies in generated code
5. **Test Thoroughly**: Run all tests and manual verification before deploying

## Reporting a Vulnerability

If you discover a security vulnerability in:
- The skill prompts
- The Python scripts
- The documentation or examples

Please report it by:

1. **Do NOT** open a public issue
2. Email repository maintainer with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

3. You will receive a response within 48 hours
4. We will work on a fix and coordinate disclosure

## Security Updates

Security updates will be:
- Released as patch versions (e.g., 1.1.1)
- Documented in CHANGELOG.md
- Announced in release notes
- Tagged as "security" in GitHub releases

## Disclosure Policy

- We follow responsible disclosure
- Security fixes will be released ASAP
- We will credit reporters (unless they prefer anonymity)
- CVEs will be filed for significant vulnerabilities

## Additional Security Resources

- [Claude.ai Security](https://www.anthropic.com/security)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [Python Security Guidelines](https://python.readthedocs.io/en/stable/library/security_warnings.html)

## Scope

### In Scope
- Vulnerabilities in scripts that could:
  - Execute unintended code
  - Access unauthorized files
  - Leak sensitive information
  - Cause denial of service

- Prompts that could:
  - Be exploited for prompt injection
  - Generate malicious code patterns
  - Bypass safety guardrails

### Out of Scope
- Issues with Claude.ai platform itself (report to Anthropic)
- General questions or feature requests (use GitHub Issues)
- Vulnerabilities in dependencies (report to dependency maintainers)
- Social engineering or phishing attempts

Thank you for helping keep PDCA AI Coding Skill secure!

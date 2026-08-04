# Security Report — Week 10 DevSecOps Pipeline

## 1. Executive Summary

This report documents the security assessment and automated security pipeline implemented for the `week10-devsecops-security` project.

The objective was to integrate security testing into the CI/CD workflow to identify vulnerable code, insecure dependencies, and exposed secrets before changes are merged into the main branch.

The implemented DevSecOps pipeline uses:
- Bandit for Static Application Security Testing (SAST)
- pip-audit for Software Composition Analysis (SCA)
- Gitleaks for secret detection

The security checks are automatically executed through GitHub Actions during pull requests to ensure insecure code does not reach production.

---

# 2. Security Tools Used

## Bandit (SAST)

Purpose:
Bandit analyzes Python source code to identify common security issues such as:
- SQL injection risks
- Weak cryptographic algorithms
- Command injection
- Hardcoded credentials

Command used:

```bash
bandit -r app/


## pip-audit (Dependency Scanning)

Purpose:
pip-audit checks third-party Python packages against known vulnerability databases and identifies dependencies with published CVEs.

Command used:

pip-audit -r requirements.txt
Gitleaks (Secret Detection)

Purpose:
Gitleaks scans source code and Git history for accidentally exposed secrets such as:

API keys
Passwords
Tokens
Credentials

Command used:

gitleaks detect --source . --verbose


pip-audit (Dependency Scanning)

Purpose:
pip-audit checks third-party Python packages against known vulnerability databases and identifies dependencies with published CVEs.

Command used:

pip-audit -r requirements.txt
Gitleaks (Secret Detection)

Purpose:
Gitleaks scans source code and Git history for accidentally exposed secrets such as:

API keys
Passwords
Tokens
Credentials

Command used:

gitleaks detect --source . --verbose

| Finding               | Severity   | Description                                       | Remediation                             |
| --------------------- | ---------- | ------------------------------------------------- | --------------------------------------- |
| SQL Injection         | Medium     | User input was directly included in SQL queries   | Use parameterized SQL queries           |
| Weak Hashing (MD5)    | High       | MD5 is insecure for password protection           | Replace with bcrypt or stronger hashing |
| Command Injection     | High       | Unsafe command execution can allow attacker input | Use secure subprocess methods           |
| Hardcoded Credentials | Low/Medium | Secrets stored directly in source code            | Move secrets to environment variables   |


4. Dependency Findings & CVEs

The dependency scan was performed using pip-audit.

Command:

pip-audit -r requirements.txt

| Package                   | Version        | Vulnerability                              | Fix              |
| ------------------------- | -------------- | ------------------------------------------ | ---------------- |
| Flask                     | 2.0.1          | PYSEC vulnerabilities                      | Upgrade Flask    |
| Requests                  | 2.25.1         | Known CVEs                                 | Upgrade requests |
| Other vulnerable packages | Older versions | Security issues from outdated dependencies | Update packages  |


After updating dependencies, pip-audit was executed again to confirm remediation.

Final scan result:

No known vulnerabilities found

5. Secret Findings

Gitleaks was used to scan the repository for exposed secrets.

Command:

gitleaks detect --source . --verbose

Initial findings included:

Hardcoded database passwords
Fake API keys
Test credentials

Remediation:

Removed secrets from source files
Added secrets to environment variables
Updated .gitignore to prevent accidental commits

Final Gitleaks scan:

No leaks found
6. Remediation Steps Taken

The following security improvements were implemented:

Code Security
Removed insecure functions
Replaced weak cryptographic methods
Applied secure coding practices
Sanitized user input
Dependency Security
Identified vulnerable packages using pip-audit
Updated dependencies to secure versions
Re-ran scans after updates
Secret Management
Removed plaintext secrets
Added environment variable usage
Added secret detection to CI/CD pipeline
CI/CD Security

GitHub Actions was configured to automatically run:

Bandit SAST scan
pip-audit dependency scan
Gitleaks secret scan

The pipeline blocks insecure code from being merged.

7. Final Result & Pipeline Verification

The final DevSecOps pipeline successfully performs automated security testing.

Pipeline checks:| Security Check       | Tool      | Status |
| -------------------- | --------- | ------ |
| Static Code Analysis | Bandit    | Passed |
| Dependency Scanning  | pip-audit | Passed |
| Secret Detection     | Gitleaks  | Passed |

Successful pipeline verification confirms that the application passes security checks before merging.

8. Lessons Learned

This project demonstrated the importance of integrating security into the software development lifecycle.

Key lessons learned:

Security testing should happen early through shift-left practices.
Automated tools reduce the chance of vulnerabilities reaching production.
CI/CD pipelines can act as security gates.
Developers share responsibility for application security.
Secrets should never be stored directly inside source code.

Implementing DevSecOps practices makes vulnerability detection faster, cheaper, and more reliable.

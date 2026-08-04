1. What is Shift Left Security?

Shift-left security means moving security testing earlier in the software development lifecycle so vulnerabilities are discovered during development instead of production.

2. What is GitHub Actions?

GitHub Actions is an automation platform that runs workflows defined in YAML files when events happen, such as pushes or pull requests.

3. What happens when a security scan fails?

The pipeline blocks the pull request from being merged until the developer fixes the vulnerability.

4. Difference between SAST and DAST?

SAST analyzes source code without running the application. DAST tests the running application from an attacker perspective.

Example:

SAST:

Bandit
Semgrep

DAST:

OWASP ZAP
Burp Suite

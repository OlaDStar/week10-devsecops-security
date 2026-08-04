# Week 10 DevSecOps Security Pipeline

## Project Overview

This project demonstrates the implementation of a secure DevSecOps pipeline for a vulnerable Python Flask application.

The objective is to integrate automated security testing into the software development lifecycle using GitHub Actions. The pipeline identifies insecure code, vulnerable dependencies, and exposed secrets before code is merged into the main branch.

The project implements three core security checks:

- Bandit — Static Application Security Testing (SAST) for Python code vulnerabilities
- pip-audit — Software Composition Analysis (SCA) for vulnerable dependencies
- GitLeaks — Secret detection for exposed credentials and sensitive information

The goal is to ensure that no insecure code reaches production.

---

## Project Structure
week10-devsecops-security/
│
├── app/
│ └── vulnerable_app.py
│
├── .github/
│ └── workflows/
│ └── security.yml
│
├── docs/
│ └── security_report.md
│
├── requirements.txt
│
└── README.md

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| Python Flask | Vulnerable web application |
| GitHub Actions | CI/CD automation |
| Bandit | Python security scanning (SAST) |
| pip-audit | Dependency vulnerability scanning |
| GitLeaks | Secret detection |
| Git | Version control |

---

## Security Pipeline Workflow

The GitHub Actions pipeline automatically runs whenever a Pull Request is created against the `main` branch.

Pipeline stages:

1. Checkout application code
2. Install Python dependencies
3. Run Bandit SAST scan
4. Run pip-audit dependency scan
5. Run GitLeaks secret detection
6. Pass or fail the Pull Request based on security results

A Pull Request is blocked if:

- High severity vulnerabilities are detected
- Vulnerable dependencies are found
- Secrets are discovered in the repository

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>

cd week10-devsecops-security

# Security Policy

## Supported Scope

Security review covers the current `main` branch of `website` and any actively maintained release assets documented in the README.

## Reporting

Do not open a public issue for secrets, private keys, personal data exposure, or exploitable vulnerabilities. Use a private contact channel with the repository owner and include:

- A concise description of the issue.
- Affected files, commits, URLs, or deployment targets.
- Reproduction steps or proof of impact.
- Whether any credential or user data may have been exposed.

## Secrets And Sensitive Data

- Never commit API keys, App Store credentials, deployment tokens, `.env` files, local databases, or machine-specific editor state.
- Keep real local environment files under `.envs/.local/` untracked. Commit only `*.example` templates.
- Rotate credentials immediately if they are exposed.
- Prefer GitHub Dependabot, secret scanning, and low-permission Actions over broad third-party access.

## Secret Scanning And Push Protection

Repository administrators should keep GitHub Secret Scanning and Push Protection enabled for this public repository. Before pushing credential-hygiene work, verify the settings in GitHub under **Settings -> Code security and analysis**.

If a real credential was ever committed, removing the file from the current tree is not enough. Rotate the affected credential first, then plan any history rewrite separately with explicit maintainer approval.

## Disclosure

Public disclosure should wait until the issue is understood, mitigated, and any affected credentials or deployments have been rotated.

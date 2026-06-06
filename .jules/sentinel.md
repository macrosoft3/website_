## 2025-05-18 - [Secure by Default & Fail Securely]
**Vulnerability:** Weak default secrets and insecure configurations in production.
**Learning:** Relying on `manage.py check --deploy` to warn about insecure settings is helpful but not sufficient for preventing misconfigured deployments. A "Secure by Default" posture ensures that hardening is on by default, but it can be bypassed if dependencies (like `SECRET_KEY`) aren't strictly enforced.
**Prevention:**
1. **Secure by Default:** Keep production hardening triggered by `not DEBUG` to ensure it's active unless explicitly disabled for development.
2. **Fail Securely:** Explicitly require critical secrets like `DJANGO_SECRET_KEY` when hardening is active. Raise a `RuntimeError` at startup if they are missing. This turns a security warning into a hard failure, preventing the application from running in an insecure state.

## 2025-05-14 - [Production Security Hardening]
**Vulnerability:** Missing security headers and insecure cookie settings in production.
**Learning:** The application was using default Django settings which are not suitable for production. Specifically, it lacked HSTS, SSL redirection, and secure flags for session and CSRF cookies.
**Prevention:** Always use `manage.py check --deploy` to identify missing production security configurations and gate these settings with an environment variable (e.g., `DJANGO_PRODUCTION`) to maintain local development ease-of-use.

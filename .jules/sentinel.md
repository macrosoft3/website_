## 2025-05-15 - Missing Production Security Settings
**Vulnerability:** The application was missing critical production security settings (HSTS, SSL Redirect, Secure Cookies) when checked with Django's deployment check.
**Learning:** Default Django settings are often insecure for production. While the README mentioned registering a SECRET_KEY, it didn't emphasize the need for other security-related settings like HSTS or secure cookies which are essential for protecting user sessions and ensuring encrypted communication.
**Prevention:** Always run `python manage.py check --deploy` before shipping and use a conditional block in `settings.py` to enable production-only security features based on an environment variable (e.g., `DJANGO_PRODUCTION`).

## 2026-05-16 - Enabling Middleware-level Optimizations
**Learning:** For mostly static Django sites, enabling `GZipMiddleware` and `ConditionalGetMiddleware` provides significant performance gains (60-70% payload reduction and 304 support) with minimal configuration and risk.
**Action:** Always check if these middlewares are present in Django projects, as they are often omitted in default or minimal setups.

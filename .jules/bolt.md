## 2026-05-30 - Middleware Optimizations for Bandwidth and Caching
**Learning:** Adding `GZipMiddleware` and `ConditionalGetMiddleware` significantly improves delivery performance. GZip reduced home page size from ~9.9KB to ~3.0KB (~70% reduction). ETags enable 304 Not Modified responses for repeat visits.
**Action:** Always ensure these middleware are present in Django projects, with GZip early in the stack and ConditionalGet after CommonMiddleware.

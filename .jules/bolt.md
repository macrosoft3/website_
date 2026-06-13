## 2026-05-30 - Middleware Optimizations for Bandwidth and Caching
**Learning:** Adding `GZipMiddleware` and `ConditionalGetMiddleware` significantly improves delivery performance. GZip reduced home page size from ~9.9KB to ~3.0KB (~70% reduction). ETags enable 304 Not Modified responses for repeat visits.
**Action:** Always ensure these middleware are present in Django projects, with GZip early in the stack and ConditionalGet after CommonMiddleware.

## 2026-06-14 - Removal of Self-Hosted Fonts for Zero-Latency Rendering
**Learning:** For a primarily Japanese site, self-hosting a variable Latin font like Inter (~48KB) accounted for ~63% of the initial page weight. Since high-quality system fonts (San Francisco, Segoe UI) are very similar, removing the web font eliminates a blocking request and significantly reduces total page weight without meaningful visual degradation.
**Action:** Prefer high-quality system font stacks for minimalist or performance-critical projects to achieve zero-latency font rendering.

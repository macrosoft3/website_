## 2026-05-17 - [Accessible Navigation and External Links]
**Learning:** Adding `aria-current="page"` to active links and `aria-label` to external links provides critical context for screen reader users that visual-only cues (like underlines or new tab behavior) do not.
**Action:** Always include `aria-current="page"` for active navigation items and describe link target behavior in `aria-label` for links with `target="_blank"`.

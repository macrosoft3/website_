## 2025-05-14 - Standardized Accessibility Patterns
**Learning:** For a multi-language (JA/EN) site, consistent accessibility patterns like `aria-current="page"` and descriptive `aria-label` for external links must be applied across all language variants to ensure a uniform experience for screen reader users.
**Action:** Always check both `ether/templates/pages/` and `ether/templates/pages/en/` when applying UI/UX enhancements.

## 2026-05-20 - Skip Link and Language Switcher Patterns
**Learning:** To make "Skip to content" links reliable with sticky headers, the `<main>` target needs `tabindex="-1"`, `scroll-margin-top` to prevent header overlap, and `outline: none` on focus to avoid visual boxes around the whole page. Additionally, language switchers should have localized `aria-label` (e.g., "Englishに切り替え") to provide clear action context for screen reader users.
**Action:** Apply these three CSS/HTML properties to the main content area and add localized labels to all language toggles.

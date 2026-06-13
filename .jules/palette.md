## 2025-05-14 - Standardized Accessibility Patterns
**Learning:** For a multi-language (JA/EN) site, consistent accessibility patterns like `aria-current="page"` and descriptive `aria-label` for external links must be applied across all language variants to ensure a uniform experience for screen reader users.
**Action:** Always check both `ether/templates/pages/` and `ether/templates/pages/en/` when applying UI/UX enhancements.

## 2025-05-15 - Enhanced Skip Link and Language Switcher Accessibility
**Learning:** To ensure functional skip links, the target element (usually `<main>`) must have `tabindex="-1"` and a `scroll-margin-top` to account for sticky headers. Additionally, language switchers need localized `aria-label` attributes to clearly communicate their purpose in the user's current context.
**Action:** Always include `tabindex="-1"` and `scroll-margin-top` for skip targets, and use contextually localized `aria-label` for language toggles.

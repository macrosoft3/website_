/* Ether — small UX polish: scrolled header state + reveal-on-view. */
(function () {
  "use strict";

  var doc = document.documentElement;
  var header = document.querySelector("[data-site-header]");

  var prefersReducedMotion =
    window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Toggle scrolled state on the sticky header. */
  if (header) {
    var lastScrolled = null;
    var updateHeader = function () {
      var isScrolled = (window.scrollY || doc.scrollTop) > 4;
      if (isScrolled !== lastScrolled) {
        header.classList.toggle("is-scrolled", isScrolled);
        lastScrolled = isScrolled;
      }
    };
    updateHeader();
    window.addEventListener("scroll", updateHeader, { passive: true });
  }

  /* Reveal elements on first intersection. */
  var revealTargets = document.querySelectorAll("[data-reveal]");
  if (!revealTargets.length) {
    return;
  }

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealTargets.forEach(function (element) {
      element.classList.add("is-visible");
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) {
          return;
        }
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
  );

  revealTargets.forEach(function (element) {
    observer.observe(element);
  });
})();

/* Ether — minimal header state only. */
(function () {
  "use strict";

  var doc = document.documentElement;
  var header = document.querySelector("[data-site-header]");

  if (!header) {
    return;
  }

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
})();

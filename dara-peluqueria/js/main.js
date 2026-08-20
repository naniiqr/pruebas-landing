document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  var dropdownParent = document.querySelector('.has-dropdown');

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  if (dropdownParent) {
    var trigger = dropdownParent.querySelector(':scope > a.top-link');
    trigger.addEventListener('click', function (e) {
      // Only intercept on small screens where the dropdown is click-driven
      if (window.matchMedia('(max-width: 720px)').matches) {
        e.preventDefault();
        dropdownParent.classList.toggle('is-open');
      }
    });
  }

  // Close mobile menu when a link is clicked
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (window.matchMedia('(max-width: 720px)').matches && a.classList.contains('top-link') === false) {
        links.classList.remove('is-open');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // ---- Delicate scroll-reveal ----
  // Respects prefers-reduced-motion: if set, elements are already fully
  // visible via CSS, so the observer simply has nothing to animate.
  var revealTargets = document.querySelectorAll('.reveal, .reveal-fade, .reveal-scale, .stagger');
  if (revealTargets.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -6% 0px' });

    revealTargets.forEach(function (el) { io.observe(el); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add('is-visible'); });
  }
});

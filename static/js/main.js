/* Portfolio interactions: theme toggle, mobile menu, project filter.
   Everything here is progressive enhancement — the site is fully usable
   without JavaScript. */
(function () {
  'use strict';

  /* ── Theme ─────────────────────────────────────────────────────── */
  var THEME_KEY = 'portfolio-theme';
  var root = document.documentElement;
  var themeBtn = document.getElementById('themeToggle');

  function isLight() { return root.getAttribute('data-theme') === 'light'; }

  function syncThemeUi() {
    if (!themeBtn) return;
    themeBtn.setAttribute('aria-label', isLight() ? 'Switch to dark theme' : 'Switch to light theme');
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', isLight() ? '#FAFAF9' : '#09090B');
  }

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = isLight() ? 'dark' : 'light';
      if (next === 'light') root.setAttribute('data-theme', 'light');
      else root.removeAttribute('data-theme');
      try { localStorage.setItem(THEME_KEY, next); } catch (e) { /* storage unavailable */ }
      syncThemeUi();
    });
  }
  syncThemeUi();

  /* ── Mobile menu ───────────────────────────────────────────────── */
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  var header = document.getElementById('siteHeader');

  function setMenu(open) {
    if (!toggle || !links) return;
    links.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('click', function (e) {
      if (header && !header.contains(e.target)) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        toggle.focus();
      }
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', function () { setMenu(false); });
  }

  /* ── Project filter ────────────────────────────────────────────── */
  var filters = document.getElementById('projectFilters');
  var grid = document.getElementById('projectsGrid');
  var status = document.getElementById('filterStatus');

  if (filters && grid) {
    filters.hidden = false;
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.project-card'));

    filters.addEventListener('click', function (e) {
      var btn = e.target.closest('.filter-btn');
      if (!btn) return;
      var wanted = btn.getAttribute('data-filter');
      var shown = 0;

      filters.querySelectorAll('.filter-btn').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b === btn));
      });
      cards.forEach(function (card) {
        var match = wanted === 'All' || card.getAttribute('data-category') === wanted;
        card.hidden = !match;
        if (match) shown += 1;
      });
      if (status) {
        status.textContent = 'Showing ' + shown + (shown === 1 ? ' project' : ' projects') +
          (wanted === 'All' ? '' : ' in ' + wanted);
      }
    });
  }
})();

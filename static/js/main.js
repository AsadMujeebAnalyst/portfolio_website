/* ══ THEME ══ */
const THEME_KEY = 'portfolio-theme';
function isLightTheme() {
  return document.documentElement.getAttribute('data-theme') === 'light';
}
function syncThemeToggleAria() {
  const btn = document.getElementById('themeToggle');
  if (!btn) return;
  btn.setAttribute('aria-label', isLightTheme() ? 'Switch to dark mode' : 'Switch to light mode');
}
function initHeroTyping() {
  const nameParts = [
    { id: 'heroNameAsad', text: 'Asad' },
    { id: 'heroNameMujeeb', text: 'Mujeeb' }
  ];
  const taglineContainer = document.getElementById('heroTitle');
  const taglineText = taglineContainer?.dataset?.text?.trim() || '';
  const nameCursor = document.getElementById('heroNameCursor');
  const taglineTextEl = document.getElementById('heroTaglineText');
  const taglineCursor = document.getElementById('heroTaglineCursor');

  if (!taglineContainer || !taglineTextEl) return;

  nameParts.forEach(part => {
    const el = document.getElementById(part.id);
    if (el) el.textContent = '';
  });
  taglineTextEl.textContent = '';
  if (nameCursor) nameCursor.classList.remove('finished');
  if (taglineCursor) taglineCursor.classList.remove('finished');

  let currentNameIndex = 0;
  let nameCharIndex = 0;

  const typeNextNameChar = () => {
    const part = nameParts[currentNameIndex];
    const el = document.getElementById(part.id);
    if (!el) return finishName();

    el.textContent += part.text[nameCharIndex++];
    if (nameCharIndex >= part.text.length) {
      currentNameIndex += 1;
      nameCharIndex = 0;
      if (currentNameIndex >= nameParts.length) {
        if (nameCursor) nameCursor.classList.add('finished');
        setTimeout(startTaglineTyping, 250);
        return;
      }
    }
    setTimeout(typeNextNameChar, 240);
  };

  const startTaglineTyping = () => {
    const words = taglineText.split(' ').filter(Boolean);
    const spans = words.map((word, index) => {
      const span = document.createElement('span');
      span.className = `hero-tagline-word ${index % 2 === 0 ? 'tagline-word-white' : 'tagline-word-gold'}`;
      taglineTextEl.appendChild(span);
      if (index < words.length - 1) {
        const spacer = document.createTextNode(' ');
        taglineTextEl.appendChild(spacer);
      }
      return span;
    });

    let currentWordIndex = 0;
    let wordCharIndex = 0;

    const typeNextTaglineChar = () => {
      if (currentWordIndex >= spans.length) {
        if (taglineCursor) taglineCursor.classList.add('finished');
        return;
      }

      const currentSpan = spans[currentWordIndex];
      const currentWord = words[currentWordIndex];
      currentSpan.textContent += currentWord[wordCharIndex++];

      if (wordCharIndex >= currentWord.length) {
        currentWordIndex += 1;
        wordCharIndex = 0;
      }
      setTimeout(typeNextTaglineChar, 90);
    };

    typeNextTaglineChar();
  };

  typeNextNameChar();
}
function applyTheme(mode) {
  if (mode === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
  } else {
    document.documentElement.removeAttribute('data-theme');
  }
  try {
    localStorage.setItem(THEME_KEY, mode);
  } catch (_) {}
  syncThemeToggleAria();
}
document.getElementById('themeToggle')?.addEventListener('click', () => {
  applyTheme(isLightTheme() ? 'dark' : 'light');
});
syncThemeToggleAria();
initHeroTyping();

/* ══ CURSOR (desktop only) ══ */
const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');
if (cursor && ring && window.matchMedia('(pointer:fine)').matches) {
  let mx = 0, my = 0, rx = 0, ry = 0;
  document.addEventListener('mousemove', e => {
    mx = e.clientX;
    my = e.clientY;
    cursor.style.left = mx + 'px';
    cursor.style.top = my + 'px';
  });
  (function loop() {
    rx += (mx - rx) * 0.11;
    ry += (my - ry) * 0.11;
    ring.style.left = rx + 'px';
    ring.style.top = ry + 'px';
    requestAnimationFrame(loop);
  })();
  const hoverSelector =
    'a,button,.theme-toggle,.skill-card,.skill-card-plain,.project-card,.cert-card,.vol-card,.volunteer-subnav-link,.vol-block,.filter-btn,.timeline-item,.timeline-icon-link,.badge-tile';
  document.querySelectorAll(hoverSelector).forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
  });
}

/* ══ NAVBAR ══ */
const navbar = document.getElementById('navbar');
if (navbar) {
  window.addEventListener('scroll', () => navbar.classList.toggle('scrolled', window.scrollY > 40), { passive: true });
}

/* ══ MOBILE NAV ══ */
const toggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

function closeNav() {
  if (!navLinks || !toggle) return;
  navLinks.classList.remove('open');
  toggle.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}

if (toggle && navLinks) {
  toggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', closeNav);
  });
}

document.addEventListener('click', e => {
  if (!navLinks?.classList.contains('open')) return;
  if (navbar?.contains(e.target)) return;
  closeNav();
});

/* ══ SCROLL REVEAL ══ */
const revealObs = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObs.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
);

(function initReveal() {
  const seen = new WeakSet();
  const markWave = (el, row, col) => {
    el.style.transitionDelay = (row + col) * 0.065 + 's';
  };

  document.querySelectorAll('.projects-grid').forEach(grid => {
    grid.querySelectorAll(':scope > .project-card').forEach((el, i) => {
      markWave(el, Math.floor(i / 3), i % 3);
      revealObs.observe(el);
      seen.add(el);
    });
  });

  document.querySelectorAll('.skill-grid-tech').forEach(grid => {
    grid.querySelectorAll(':scope > .skill-card').forEach((el, i) => {
      markWave(el, Math.floor(i / 6), i % 6);
      revealObs.observe(el);
      seen.add(el);
    });
  });

  document.querySelectorAll('.skill-grid-biz').forEach(grid => {
    grid.querySelectorAll(':scope > .skill-card-plain').forEach((el, i) => {
      markWave(el, Math.floor(i / 4), i % 4);
      revealObs.observe(el);
      seen.add(el);
    });
  });

  let idx = 0;
  document.querySelectorAll('.reveal, .timeline-item, .cert-card, .vol-card, .vol-block').forEach(el => {
    if (seen.has(el)) return;
    if (el.closest('.projects-grid')) return;
    el.style.transitionDelay = idx++ * 0.045 + 's';
    revealObs.observe(el);
  });
})();

/* ══ FLASH ══ */
document.querySelectorAll('.flash-dismiss').forEach(btn => {
  btn.addEventListener('click', () => btn.closest('.flash')?.remove());
});
document.querySelectorAll('.flash').forEach(f => setTimeout(() => f.remove(), 5000));

/* ══ PROJECT FILTER NAV (fade) ══ */
(function filterNavFade() {
  const filt = document.querySelector('.projects-filter');
  const grid = document.querySelector('.projects-grid');
  if (!filt || !grid) return;
  filt.querySelectorAll('a.filter-btn').forEach(a => {
    a.addEventListener('click', e => {
      if (a.classList.contains('active')) {
        e.preventDefault();
        return;
      }
      e.preventDefault();
      grid.classList.add('filter-fade-out');
      const href = a.getAttribute('href');
      setTimeout(() => {
        window.location.href = href;
      }, 200);
    });
  });
})();

document.addEventListener('keydown', e => {
  if (e.key !== 'Escape') return;
  closeNav();
});

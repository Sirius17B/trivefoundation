/* ═══════════════════════════════════════════════════════════
   THRIVE v5  ·  main.js
   Security · Nav · Carousel · League · Tech · Video
   Admin Auth · CMS · Counters · Toast · Scroll Reveal
   ═══════════════════════════════════════════════════════════ */
'use strict';

/* ── SECURITY ────────────────────────────────────────────────────────────── */
(function () {
  /* Clickjacking prevention */
  if (window.top !== window.self) {
    try { window.top.location = window.self.location; } catch (e) { /* cross-origin */ }
  }

  /* XSS sanitiser — always escape user content before DOM insertion */
  window.sanitize = function (str) {
    const d = document.createElement('div');
    d.textContent = String(str ?? '');
    return d.innerHTML;
  };

  /* Brute-force login rate limiter */
  const _f = { n: 0, until: 0 };
  window._loginFail = function () {
    _f.n++;
    if (_f.n >= 5) { _f.until = Date.now() + 60000; _f.n = 0; }
  };
  window._locked = function () { return Date.now() < _f.until; };
})();

/* ── NAV: scroll + hamburger ─────────────────────────────────────────────── */
window.initNavInteractions = function () {
  const nav = document.querySelector('.nav');
  if (!nav || nav.dataset.ready === '1') return;
  nav.dataset.ready = '1';

  const update = () => nav.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', update, { passive: true });
  update();

  const btn   = nav.querySelector('.nav-hamburger');
  const links = nav.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', () => {
      const o = links.classList.toggle('open');
      btn.classList.toggle('open', o);
      btn.setAttribute('aria-expanded', String(o));
    });
    document.addEventListener('click', e => {
      if (!nav.contains(e.target)) {
        links.classList.remove('open');
        btn.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
    links.querySelectorAll('.nav-link, .nav-cta').forEach(a => {
      a.addEventListener('click', () => {
        links.classList.remove('open');
        btn.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* Active link highlighting */
  const p = location.pathname.split('/').pop() || 'index.html';
  nav.querySelectorAll('.nav-link').forEach(a => {
    const h = a.getAttribute('href') || '';
    if (h === p || (p === '' && h === 'index.html') || (p === 'index.html' && h === 'index.html')) {
      a.classList.add('active');
    }
  });
};

document.addEventListener('thrive:nav-injected', () => window.initNavInteractions?.());
document.addEventListener('DOMContentLoaded',     () => window.initNavInteractions?.());

/* ── SCROLL REVEAL ───────────────────────────────────────────────────────── */
(function () {
  const els = document.querySelectorAll('.fade-up');
  if (!els.length) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
    });
  }, { threshold: .08, rootMargin: '0px 0px -28px 0px' });
  els.forEach(el => io.observe(el));
})();

/* ── TOAST ───────────────────────────────────────────────────────────────── */
window.showToast = function (msg, type = '', dur = 3200) {
  let t = document.querySelector('.toast');
  if (!t) {
    t = document.createElement('div');
    t.className = 'toast';
    t.setAttribute('role', 'alert');
    t.setAttribute('aria-live', 'polite');
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.className = 'toast' + (type ? ' ' + type : '');
  t.classList.add('show');
  clearTimeout(t._t);
  t._t = setTimeout(() => t.classList.remove('show'), dur);
};

/* ── ANIMATED STATS COUNTER ──────────────────────────────────────────────── */
window.initCounters = function () {
  const els = document.querySelectorAll('[data-count]');
  if (!els.length) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const target = parseInt(el.dataset.count, 10);
      const suffix = el.dataset.suffix || '';
      const dur = 1600;
      let start = null;
      const tick = ts => {
        if (!start) start = ts;
        const p = Math.min((ts - start) / dur, 1);
        const ease = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(ease * target) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      io.unobserve(el);
    });
  }, { threshold: .4 });
  els.forEach(el => io.observe(el));
};

/* ── CAROUSEL ────────────────────────────────────────────────────────────── */
window.initCarousel = function (wrapSelector, opts = {}) {
  const wrap = document.querySelector(wrapSelector);
  if (!wrap) return;
  const viewport = wrap.querySelector('.carousel-viewport');
  const track    = wrap.querySelector('.carousel-track');
  const cards    = Array.from(track?.querySelectorAll('.c-card') || []);
  const prevBtn  = wrap.querySelector('.carousel-prev');
  const nextBtn  = wrap.querySelector('.carousel-next');
  const dotsWrap = wrap.querySelector('.carousel-dots');
  if (!cards.length || !track) return;

  const gap = 14;
  let current = 0, timer = null;

  const getCardW   = () => (cards[0]?.offsetWidth || 280) + gap;
  const getVisible = () => Math.max(1, Math.floor((viewport?.offsetWidth || wrap.offsetWidth) / getCardW()));
  const maxIdx     = () => Math.max(0, cards.length - getVisible());

  const dots = dotsWrap ? cards.map((_, i) => {
    const d = document.createElement('button');
    d.className = 'c-dot';
    d.setAttribute('aria-label', 'Go to slide ' + (i + 1));
    d.addEventListener('click', () => go(i));
    dotsWrap.appendChild(d);
    return d;
  }) : [];

  function go(idx) {
    current = Math.max(0, Math.min(idx, maxIdx()));
    track.style.transform = `translateX(-${current * getCardW()}px)`;
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
    if (prevBtn) prevBtn.disabled = current === 0;
    if (nextBtn) nextBtn.disabled = current === maxIdx();
  }

  if (prevBtn) prevBtn.addEventListener('click', () => { clearInterval(timer); go(current - 1); startTimer(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { clearInterval(timer); go(current + 1); startTimer(); });

  function startTimer() {
    if (opts.autoplay === false) return;
    timer = setInterval(() => go(current >= maxIdx() ? 0 : current + 1), opts.interval || 4800);
  }

  wrap.addEventListener('mouseenter', () => clearInterval(timer));
  wrap.addEventListener('mouseleave', startTimer);

  /* Touch swipe */
  let sx = 0;
  track.addEventListener('touchstart', e => { sx = e.touches[0].clientX; clearInterval(timer); }, { passive: true });
  track.addEventListener('touchend', e => {
    const d = sx - e.changedTouches[0].clientX;
    if (Math.abs(d) > 42) go(d > 0 ? current + 1 : current - 1);
    startTimer();
  });

  go(0); startTimer();
  window.addEventListener('resize', () => go(current));
};

/* ── STORAGE HELPERS ─────────────────────────────────────────────────────── */
function _deepClone(v) { return JSON.parse(JSON.stringify(v)); }

async function _loadFromStorage(key, fallback) {
  try {
    const stored = await window.storage?.get(key);
    return stored ? JSON.parse(stored.value) : _deepClone(fallback);
  } catch {
    return _deepClone(fallback);
  }
}

async function _saveToStorage(key, payload) {
  try { await window.storage?.set(key, JSON.stringify(payload)); } catch { /* no storage */ }
}

/* ── LEAGUE ENGINE ───────────────────────────────────────────────────────── */
const _LK = 'thrive_v5_league_';
const _DEMO_BOYS = {
  teams: ['SS3 Boys', 'SS2 Boys', 'SS1 Boys A', 'SS1 Boys B', 'JSS3 Boys', 'JSS2 Boys', 'JSS1 Boys', 'Staff FC'],
  results: [
    { home:'SS3 Boys',   hg:4, ag:3, away:'JSS3 Boys'   },
    { home:'SS2 Boys',   hg:2, ag:1, away:'SS1 Boys A'  },
    { home:'SS1 Boys B', hg:3, ag:0, away:'JSS2 Boys'   },
    { home:'Staff FC',   hg:1, ag:1, away:'JSS1 Boys'   },
    { home:'SS3 Boys',   hg:2, ag:2, away:'SS2 Boys'    },
    { home:'JSS3 Boys',  hg:0, ag:2, away:'SS1 Boys A'  },
  ],
};
const _DEMO_GIRLS = {
  teams: ['SS2 Girls', 'SS1 Girls', 'SS3 Girls', 'JSS3 Girls', 'JSS2 Girls', 'JSS1 Girls'],
  results: [
    { home:'SS2 Girls', hg:3, ag:1, away:'SS1 Girls'  },
    { home:'SS3 Girls', hg:2, ag:0, away:'JSS3 Girls' },
    { home:'SS2 Girls', hg:2, ag:0, away:'SS3 Girls'  },
    { home:'SS1 Girls', hg:2, ag:1, away:'JSS3 Girls' },
  ],
};

window.LeagueEngine = {
  _d: {},
  async load(lg) {
    this._d[lg] = await _loadFromStorage(_LK + lg, lg === 'boys' ? _DEMO_BOYS : _DEMO_GIRLS);
    return this._d[lg];
  },
  async save(lg) { await _saveToStorage(_LK + lg, this._d[lg]); },
  get(lg) { return this._d[lg] || { teams: [], results: [] }; },
  addResult(lg, home, away, hg, ag) {
    const d = this.get(lg);
    if (!d.teams.includes(home)) d.teams.push(sanitize(home));
    if (!d.teams.includes(away)) d.teams.push(sanitize(away));
    d.results.push({ home, away, hg: +hg, ag: +ag });
    this.save(lg);
  },
  removeResult(lg, idx) { this.get(lg).results.splice(idx, 1); this.save(lg); },
  addTeam(lg, name) {
    const d = this.get(lg);
    if (d.teams.includes(name)) return false;
    d.teams.push(name); this.save(lg); return true;
  },
  removeTeam(lg, name) {
    const d = this.get(lg);
    d.teams   = d.teams.filter(t => t !== name);
    d.results = d.results.filter(r => r.home !== name && r.away !== name);
    this.save(lg);
  },
  buildTable(lg) {
    const d = this.get(lg);
    const s = {};
    d.teams.forEach(t => { s[t] = { p:0, w:0, d:0, l:0, gf:0, ga:0, form:[] }; });
    d.results.forEach(({ home, away, hg, ag }) => {
      const h = +hg, a = +ag;
      if (isNaN(h) || isNaN(a)) return;
      [home, away].forEach(t => { if (!s[t]) s[t] = { p:0, w:0, d:0, l:0, gf:0, ga:0, form:[] }; });
      s[home].p++; s[away].p++;
      s[home].gf += h; s[home].ga += a;
      s[away].gf += a; s[away].ga += h;
      if (h > a) { s[home].w++; s[away].l++; s[home].form.push('W'); s[away].form.push('L'); }
      else if (h < a) { s[away].w++; s[home].l++; s[home].form.push('L'); s[away].form.push('W'); }
      else { s[home].d++; s[away].d++; s[home].form.push('D'); s[away].form.push('D'); }
    });
    return Object.entries(s)
      .map(([n, x]) => ({ name:n, ...x, gd:x.gf-x.ga, pts:x.w*3+x.d, form:x.form.slice(-5) }))
      .sort((a, b) => b.pts - a.pts || b.gd - a.gd || b.gf - a.gf);
  },
};

/* ── TECH ENGINE ──────────────────────────────────────────────────────────── */
const _TK = 'thrive_v5_tech_';
const _DEMO_TECH = {
  participants: [
    { name:'Amara Okafor',    class:'SS3', score:92, project:'Weather App'    },
    { name:'Tobenna Eze',     class:'SS2', score:88, project:'School Portal'  },
    { name:'Chidera Nwosu',   class:'SS3', score:85, project:'Quiz Platform'  },
    { name:'Fatima Al-Hassan',class:'SS1', score:82, project:'Recipe Finder'  },
    { name:'David Osei',      class:'SS2', score:79, project:'Budget Tracker' },
    { name:'Ngozi Adeleke',   class:'JSS3',score:76, project:'To-Do App'      },
    { name:'Emeka Chukwu',    class:'SS1', score:73, project:'Calculator'     },
  ],
};

window.TechEngine = {
  _d: null,
  async load() { this._d = await _loadFromStorage(_TK + 'data', _DEMO_TECH); return this._d; },
  async save() { await _saveToStorage(_TK + 'data', this._d); },
  get() { return this._d || _DEMO_TECH; },
  getTop(n = 5) { return [...this.get().participants].sort((a, b) => b.score - a.score).slice(0, n); },
  add(name, cls, score, project) {
    if (!this._d) this._d = _deepClone(_DEMO_TECH);
    this._d.participants.push({ name, class: cls, score: +score, project });
    this.save();
  },
  remove(idx) { this.get().participants.splice(idx, 1); this.save(); },
};

/* ── VIDEO ENGINE ────────────────────────────────────────────────────────── */
const _VK = 'thrive_v5_videos_';
window.VideoEngine = {
  _d: null,
  async load() { this._d = await _loadFromStorage(_VK + 'list', { videos: [] }); return this._d; },
  async save() { await _saveToStorage(_VK + 'list', this._d); },
  get() { return (this._d || { videos: [] }).videos; },
  add(title, dataUrl, type) {
    const vids = this._d = this._d || { videos: [] };
    vids.videos.push({ title, dataUrl, type, date: new Date().toLocaleDateString() });
    this.save();
  },
  remove(idx) { this.get().splice(idx, 1); this.save(); },
};

/* ── ADMIN AUTH ──────────────────────────────────────────────────────────── */
/*
  PIN hash: btoa('thrive-2025-admin') = 'dGhyaXZlLTIwMjUtYWRtaW4='
  To change PIN:
    1. Open js/main.js
    2. Replace _AH value with btoa('thrive-NEWPIN-admin')
    3. Save and redeploy
*/
const _AH = 'dGhyaXZlLTIwMjUtYWRtaW4=';

window.AdminAuth = {
  _k: 'thrive_v5_admin_session',
  isLoggedIn()  { return sessionStorage.getItem(this._k) === '1'; },
  login(pin)    {
    if (window._locked()) return 'locked';
    if (btoa('thrive-' + pin + '-admin') === _AH) {
      sessionStorage.setItem(this._k, '1');
      return true;
    }
    window._loginFail();
    return false;
  },
  logout()      { sessionStorage.removeItem(this._k); },
};

/* Auto-restore admin UI on page load if session is still active */
document.addEventListener('DOMContentLoaded', () => {
  if (!window.AdminAuth.isLoggedIn()) return;
  setTimeout(() => {
    const tb = document.getElementById('cms-toolbar');
    if (tb) tb.style.display = 'flex';
    const lbl = document.getElementById('nav-admin-lbl');
    if (lbl) lbl.textContent = 'Edit Content';
    const btn = document.getElementById('nav-admin-btn');
    if (btn) {
      btn.style.display     = 'inline-flex';
      btn.style.background  = 'var(--green-100)';
      btn.style.borderColor = 'var(--green-600)';
      btn.style.color       = 'var(--green-700)';
    }
    document.querySelectorAll('.admin-only').forEach(el => el.style.display = 'block');
    window._enableInlineEdit?.();
  }, 120);
});

/* ── CMS ─────────────────────────────────────────────────────────────────── */
const _CK = 'thrive_v5_cms_';
window.CMS = {
  _d: {},
  async load() {
    this._d = await _loadFromStorage(_CK + 'data', {});
    return this._d;
  },
  async save() { await _saveToStorage(_CK + 'data', this._d); },
  get(key, fallback = '') { return this._d[key] ?? fallback; },
  set(key, val) { this._d[key] = val; this.save(); },
  apply() {
    document.querySelectorAll('[data-cms]').forEach(el => {
      const key = el.dataset.cms;
      const val = this.get(key);
      if (!val) return;
      if (el.tagName === 'IMG') {
        el.src = val;
        if (el.dataset.cmsAlt) el.alt = this.get(el.dataset.cmsAlt, el.alt);
      } else {
        el.textContent = val;
      }
    });
    /* Apply org name override everywhere */
    const cfg  = window.SITE_CONFIG;
    const name = this.get('org_name', cfg?.ORG_NAME);
    if (name) document.querySelectorAll('[data-org-name]').forEach(el => el.textContent = name);
  },
};

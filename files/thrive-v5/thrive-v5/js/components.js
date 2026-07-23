/* ═══════════════════════════════════════════════
   THRIVE v5  ·  components.js
   Shared nav, footer, admin login, CMS toolbar
   Rebrand: change ORG_NAME in config.js only.
   ═══════════════════════════════════════════════ */
'use strict';

/* ── LOGO LOCKUP ──────────────────────────────────────────────────────────── */
window.LOGO_HTML = function (dark) {
  const cfg  = window.SITE_CONFIG || {};
  const name = cfg.ORG_NAME    || 'THRIVE';
  const tag  = cfg.ORG_TAGLINE || 'Raising Champions';
  const nameCol = dark ? '#FFFFFF' : 'var(--ink-900)';
  const tagCol  = dark ? '#6EE7A0' : 'var(--green-600)';
  return `<span class="logo-lockup" aria-label="${name} — ${tag}" role="img"
    style="display:inline-flex;align-items:center;gap:10px;text-decoration:none">
    <img src="assets/tree-logo.png" alt="" aria-hidden="true"
         style="height:44px;width:auto;object-fit:contain;flex-shrink:0">
    <span class="nav-logo-text">
      <span class="nav-logo-name" data-org-name style="color:${nameCol}">${name}</span>
      <span class="nav-logo-tag" style="color:${tagCol}">${tag}</span>
    </span>
  </span>`;
};

/* ── NAV ──────────────────────────────────────────────────────────────────── */
window.injectNav = function () {
  const el = document.querySelector('.nav');
  if (!el) return;
  const cfg  = window.SITE_CONFIG || {};
  const name = cfg.ORG_NAME || 'THRIVE';
  el.innerHTML = `
    <a class="skip-link" href="#main">Skip to main content</a>
    <div class="nav-inner">
      <a href="index.html" class="nav-logo" aria-label="${name} — Home">
        ${window.LOGO_HTML(false)}
      </a>
      <nav class="nav-links" role="navigation" aria-label="Main navigation" id="nav-menu">
        <a href="index.html"      class="nav-link">Home</a>
        <a href="about.html"      class="nav-link">About</a>
        <a href="activities.html" class="nav-link">Activities</a>
        <a href="gallery.html"    class="nav-link">Gallery</a>
        <a href="contact.html"    class="nav-link">Contact</a>
        <a href="donate.html"     class="nav-cta">Donate</a>
      </nav>
      <div style="display:flex;align-items:center;gap:8px;flex-shrink:0">
        <button id="nav-admin-btn" onclick="window._openAdminLogin()"
          aria-label="Admin login"
          style="display:none;background:var(--surface-2);border:1px solid var(--border-dark);
                 color:var(--ink-500);padding:6px 13px;border-radius:var(--r-sm);
                 font-size:.78rem;font-weight:600;align-items:center;gap:5px;
                 cursor:pointer;transition:all var(--t-fast)">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <span id="nav-admin-lbl">Admin</span>
        </button>
        <button class="nav-hamburger" aria-label="Toggle menu"
                aria-expanded="false" aria-controls="nav-menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>`;

  _setAdminNavState(Boolean(window.AdminAuth?.isLoggedIn()));
  document.dispatchEvent(new CustomEvent('thrive:nav-injected'));
};

function _setAdminNavState(on) {
  const btn = document.getElementById('nav-admin-btn');
  const lbl = document.getElementById('nav-admin-lbl');
  if (!btn || !lbl) return;
  if (on) {
    btn.style.display       = 'inline-flex';
    btn.style.background    = 'var(--green-100)';
    btn.style.borderColor   = 'var(--green-600)';
    btn.style.color         = 'var(--green-700)';
    lbl.textContent         = 'Edit Content';
  } else {
    btn.style.display       = 'none';
  }
}

/* ── ADMIN UI (login modal + CMS toolbar) ────────────────────────────────── */
window.injectAdminUI = function () {
  if (document.getElementById('_thrive-admin-ui')) return;
  const wrap = document.createElement('div');
  wrap.id = '_thrive-admin-ui';
  wrap.innerHTML = `
<!-- ── Admin login modal ── -->
<div id="login-modal" class="modal-bg" role="dialog" aria-modal="true"
     aria-labelledby="login-modal-title" style="display:none">
  <div class="modal-box" style="max-width:400px">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:.6rem">
      <div style="width:36px;height:36px;border-radius:var(--r-md);background:var(--green-100);
                  display:flex;align-items:center;justify-content:center;flex-shrink:0">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--green-600)" stroke-width="2">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
        </svg>
      </div>
      <h2 id="login-modal-title" style="font-size:1.05rem">Admin Access</h2>
    </div>
    <p style="font-size:.85rem;color:var(--ink-500);margin-bottom:1rem">
      Enter the admin PIN to manage content and results.
    </p>
    <div id="login-err" role="alert"
         style="display:none;background:var(--red-100);border:1px solid #FECACA;
                border-radius:var(--r-sm);padding:8px 12px;font-size:.82rem;
                color:var(--red-600);margin-bottom:10px"></div>
    <div class="fg" style="margin-bottom:14px">
      <label for="admin-pin-inp" style="font-size:.84rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:5px">PIN</label>
      <input type="password" id="admin-pin-inp" autocomplete="current-password"
             maxlength="20" placeholder="Enter admin PIN" class="fi">
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn btn-green" onclick="window._doAdminLogin()">Sign In</button>
      <button class="btn btn-ghost" onclick="window._closeLoginModal()">Cancel</button>
    </div>
    <p style="font-size:.74rem;color:var(--ink-300);margin-top:12px">
      PIN available to authorised administrators only.
    </p>
  </div>
</div>

<!-- ── CMS editing toolbar ── -->
<div id="cms-toolbar" class="cms-toolbar" role="toolbar" aria-label="Content editor">
  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6EE7A0" stroke-width="2" aria-hidden="true">
    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
  </svg>
  <span style="color:rgba(255,255,255,.65);font-size:.82rem">
    Edit mode — click any highlighted text or image to edit
  </span>
  <button onclick="window._cmsSaveAll()" class="btn btn-green btn-sm">Save All Changes</button>
  <button onclick="window._openCMSPanel()" class="btn btn-sm"
          style="background:rgba(255,255,255,.1);color:#fff">Site Settings</button>
  <button onclick="window._adminLogout()" class="btn btn-sm"
          style="background:transparent;color:rgba(255,255,255,.45);border:1px solid rgba(255,255,255,.15)">
    Log Out
  </button>
</div>

<!-- ── CMS Settings panel ── -->
<div id="cms-panel-bg"
     style="display:none;position:fixed;inset:0;z-index:1300;background:rgba(15,25,35,.5)"
     onclick="if(event.target===this)window._closeCMSPanel()">
  <div id="cms-panel" role="dialog" aria-modal="true" aria-labelledby="cms-panel-title"
       style="position:absolute;bottom:0;left:0;right:0;background:var(--surface);
              border-radius:var(--r-2xl) var(--r-2xl) 0 0;
              max-height:90svh;overflow-y:auto;padding:24px clamp(16px,4vw,40px) 40px">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px">
      <h2 id="cms-panel-title" style="font-size:1.1rem">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--teal-600)" stroke-width="2" style="vertical-align:middle;margin-right:6px">
          <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
          <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
        </svg>
        Site Settings
      </h2>
      <button onclick="window._closeCMSPanel()" aria-label="Close"
              style="background:var(--surface-2);border:none;border-radius:50%;
                     width:32px;height:32px;font-size:1.1rem;cursor:pointer;color:var(--ink-500)">✕</button>
    </div>
    <div style="display:flex;gap:4px;border-bottom:1px solid var(--border);margin-bottom:20px;flex-wrap:wrap" role="tablist">
      <button class="cms-t active" onclick="cmsTab(0,this)">Identity</button>
      <button class="cms-t" onclick="cmsTab(1,this)">Homepage</button>
      <button class="cms-t" onclick="cmsTab(2,this)">Stats</button>
      <button class="cms-t" onclick="cmsTab(3,this)">Donate</button>
      <button class="cms-t" onclick="cmsTab(4,this)">Footer</button>
    </div>
    <div id="cms-panels-wrap">
      <!-- Identity -->
      <div class="cms-panel active">
        <p class="cms-note">Changing the name here updates it everywhere — nav, footer, all pages. Refresh other tabs to see it.</p>
        <div class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Organisation Name</label>
               <input id="cms-org-name" type="text" class="fi" placeholder="THRIVE"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Tagline</label>
               <input id="cms-org-tagline" type="text" class="fi" placeholder="Raising Champions"></div>
        </div>
        <div style="margin-bottom:12px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Mission Statement</label>
          <input id="cms-org-mission" type="text" class="fi">
        </div>
        <div style="margin-bottom:16px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Contact Email</label>
          <input id="cms-org-email" type="email" class="fi">
        </div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('identity')">Save Identity</button>
      </div>
      <!-- Homepage -->
      <div class="cms-panel">
        <div class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Hero Line 1</label>
               <input id="cms-hero1" type="text" class="fi" placeholder="A Time"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Hero Line 2 (italic)</label>
               <input id="cms-hero2" type="text" class="fi" placeholder="To Build"></div>
        </div>
        <div style="margin-bottom:12px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Hero Body</label>
          <textarea id="cms-hero-body" rows="2" class="fi" style="resize:vertical"></textarea>
        </div>
        <div style="margin-bottom:12px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Parallax Quote</label>
          <textarea id="cms-hero-quote" rows="2" class="fi" style="resize:vertical"></textarea>
        </div>
        <div style="margin-bottom:16px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Quote Attribution</label>
          <input id="cms-quote-cite" type="text" class="fi">
        </div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('homepage')">Save Homepage</button>
      </div>
      <!-- Stats -->
      <div class="cms-panel">
        <p style="font-size:.82rem;color:var(--ink-500);margin-bottom:14px">These numbers animate on the homepage stats bar.</p>
        <div class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Youth Trained</label><input id="cms-stat-youth" type="number" min="0" class="fi"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Label</label><input id="cms-stat-youth-lbl" type="text" class="fi"></div>
        </div>
        <div class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Event Hours</label><input id="cms-stat-hours" type="number" min="0" class="fi"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Label</label><input id="cms-stat-hours-lbl" type="text" class="fi"></div>
        </div>
        <div class="cms-field-row" style="margin-bottom:16px">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Partners</label><input id="cms-stat-partners" type="number" min="0" class="fi"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Label</label><input id="cms-stat-partners-lbl" type="text" class="fi"></div>
        </div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('stats')">Save Stats</button>
      </div>
      <!-- Donate -->
      <div class="cms-panel">
        <div style="margin-bottom:12px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Donate Page Title</label>
          <input id="cms-donate-title" type="text" class="fi">
        </div>
        <div style="margin-bottom:16px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Payment Reference Note</label>
          <input id="cms-bank-confirm" type="text" class="fi">
        </div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('donate')">Save Donate</button>
      </div>
      <!-- Footer -->
      <div class="cms-panel">
        <div style="margin-bottom:12px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Footer Tagline</label>
          <textarea id="cms-footer-tag" rows="2" class="fi" style="resize:vertical"></textarea>
        </div>
        <div style="margin-bottom:16px">
          <label style="font-size:.82rem;font-weight:600;color:var(--ink-900);display:block;margin-bottom:4px">Footer Quote</label>
          <input id="cms-footer-quote" type="text" class="fi">
        </div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('footer')">Save Footer</button>
      </div>
    </div>
  </div>
</div>`;
  document.body.appendChild(wrap);

  /* Keyboard shortcuts */
  if (!window._adminShortcutBound) {
    window._adminShortcutBound = true;
    document.addEventListener('keydown', e => {
      if (String(e.key || '').toLowerCase() === 'a' && (e.ctrlKey || e.metaKey) && e.shiftKey) {
        e.preventDefault();
        window._openAdminLogin();
      }
      if (e.key === 'Escape') {
        window._closeLoginModal();
        window._closeCMSPanel();
      }
    });
  }
  document.getElementById('admin-pin-inp')?.addEventListener('keydown', e => {
    if (e.key === 'Enter') window._doAdminLogin();
  });
};

/* ── Global admin controls ──────────────────────────────────────────────── */
window._openAdminLogin = function () {
  if (window.AdminAuth?.isLoggedIn()) { window._toggleInlineEdit(); return; }
  const m = document.getElementById('login-modal');
  if (m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; document.getElementById('admin-pin-inp')?.focus(); }
};
window._closeLoginModal = function () {
  const m = document.getElementById('login-modal');
  if (m) { m.style.display = 'none'; document.body.style.overflow = ''; }
  const err = document.getElementById('login-err');
  if (err) err.style.display = 'none';
  const inp = document.getElementById('admin-pin-inp');
  if (inp) inp.value = '';
};
window._doAdminLogin = function () {
  if (window._locked()) { _showLoginErr('Too many attempts. Wait 60 seconds.'); return; }
  const pin    = document.getElementById('admin-pin-inp')?.value || '';
  const result = window.AdminAuth?.login(pin);
  if (result === true) {
    window._closeLoginModal();
    _setAdminNavState(true);
    const tb = document.getElementById('cms-toolbar');
    if (tb) tb.style.display = 'flex';
    window._enableInlineEdit();
    window.showToast?.('Admin mode active — click highlighted text or images to edit', 'ok');
    document.querySelectorAll('.admin-only').forEach(el => el.style.display = 'block');
    document.dispatchEvent(new CustomEvent('thrive:admin-state', { detail: { loggedIn: true } }));
  } else {
    _showLoginErr(window._locked() ? 'Locked — wait 60 seconds.' : 'Incorrect PIN.');
    const inp = document.getElementById('admin-pin-inp');
    if (inp) inp.value = '';
  }
};
function _showLoginErr(msg) {
  const e = document.getElementById('login-err');
  if (e) { e.textContent = msg; e.style.display = 'block'; }
}
window._adminLogout = function () {
  window.AdminAuth?.logout();
  _setAdminNavState(false);
  const tb = document.getElementById('cms-toolbar');
  if (tb) tb.style.display = 'none';
  window._disableInlineEdit();
  document.querySelectorAll('.admin-only').forEach(el => el.style.display = 'none');
  document.dispatchEvent(new CustomEvent('thrive:admin-state', { detail: { loggedIn: false } }));
  window.showToast?.('Logged out');
};
window._openCMSPanel = function () {
  const bg = document.getElementById('cms-panel-bg');
  if (bg) { bg.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  const d = window.CMS?._d || {};
  const cfg = window.SITE_CONFIG || {};
  const s = cfg.STATS || {};
  const setV = (id, val) => { const el = document.getElementById(id); if (el) el.value = val || ''; };
  setV('cms-org-name',        d.org_name         || cfg.ORG_NAME    || '');
  setV('cms-org-tagline',     d.org_tagline       || cfg.ORG_TAGLINE || '');
  setV('cms-org-mission',     d.org_mission       || cfg.ORG_MISSION || '');
  setV('cms-org-email',       d.org_email         || cfg.ORG_EMAIL   || '');
  setV('cms-hero1',           d.hero_line1        || cfg.HERO_LINE1  || '');
  setV('cms-hero2',           d.hero_line2        || cfg.HERO_LINE2  || '');
  setV('cms-hero-body',       d.hero_body         || cfg.HERO_BODY   || '');
  setV('cms-hero-quote',      d.hero_quote        || '');
  setV('cms-quote-cite',      d.hero_quote_cite   || '');
  setV('cms-stat-youth',      d.stat_youth_count  ?? s.youth?.value    ?? '');
  setV('cms-stat-youth-lbl',  d.stat_youth_label  || s.youth?.label    || '');
  setV('cms-stat-hours',      d.stat_hours_count  ?? s.hours?.value    ?? '');
  setV('cms-stat-hours-lbl',  d.stat_hours_label  || s.hours?.label    || '');
  setV('cms-stat-partners',   d.stat_partners_count ?? s.partners?.value ?? '');
  setV('cms-stat-partners-lbl', d.stat_partners_label || s.partners?.label || '');
  setV('cms-donate-title',    d.donate_title      || '');
  setV('cms-bank-confirm',    d.bank_confirm      || cfg.BANK?.note   || '');
  setV('cms-footer-tag',      d.footer_tagline    || '');
  setV('cms-footer-quote',    d.footer_quote      || '');
};
window._closeCMSPanel = function () {
  const bg = document.getElementById('cms-panel-bg');
  if (bg) { bg.style.display = 'none'; document.body.style.overflow = ''; }
};
window.cmsTab = function (idx, btn) {
  document.querySelectorAll('.cms-t').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  document.querySelectorAll('#cms-panels-wrap .cms-panel').forEach((p, i) => {
    p.style.display = i === idx ? 'block' : 'none';
    p.classList.toggle('active', i === idx);
  });
};
window.saveCMS = function (section) {
  if (!window.CMS) return;
  const g = id => document.getElementById(id)?.value?.trim() || '';
  if (section === 'identity') {
    window.CMS.set('org_name',    g('cms-org-name'));
    window.CMS.set('org_tagline', g('cms-org-tagline'));
    window.CMS.set('org_mission', g('cms-org-mission'));
    window.CMS.set('org_email',   g('cms-org-email'));
    const name = g('cms-org-name') || window.SITE_CONFIG?.ORG_NAME || 'THRIVE';
    document.querySelectorAll('[data-org-name]').forEach(el => el.textContent = name);
  }
  if (section === 'homepage') {
    window.CMS.set('hero_line1',      g('cms-hero1'));
    window.CMS.set('hero_line2',      g('cms-hero2'));
    window.CMS.set('hero_body',       g('cms-hero-body'));
    window.CMS.set('hero_quote',      g('cms-hero-quote'));
    window.CMS.set('hero_quote_cite', g('cms-quote-cite'));
  }
  if (section === 'stats') {
    window.CMS.set('stat_youth_count',    g('cms-stat-youth'));
    window.CMS.set('stat_youth_label',    g('cms-stat-youth-lbl'));
    window.CMS.set('stat_hours_count',    g('cms-stat-hours'));
    window.CMS.set('stat_hours_label',    g('cms-stat-hours-lbl'));
    window.CMS.set('stat_partners_count', g('cms-stat-partners'));
    window.CMS.set('stat_partners_label', g('cms-stat-partners-lbl'));
  }
  if (section === 'donate') {
    window.CMS.set('donate_title',  g('cms-donate-title'));
    window.CMS.set('bank_confirm',  g('cms-bank-confirm'));
  }
  if (section === 'footer') {
    window.CMS.set('footer_tagline', g('cms-footer-tag'));
    window.CMS.set('footer_quote',   g('cms-footer-quote'));
    document.querySelectorAll('[data-cms="footer_tagline"]').forEach(el => el.textContent = g('cms-footer-tag'));
    document.querySelectorAll('[data-cms="footer_quote"]').forEach(el => el.textContent = g('cms-footer-quote'));
  }
  window.CMS.apply();
  window.showToast?.('✓ Saved', 'ok');
};
window._cmsSaveAll = function () {
  document.querySelectorAll('[data-cms][contenteditable="true"]').forEach(el => {
    window.CMS?.set(el.dataset.cms, el.innerText.trim());
  });
  window.showToast?.('✓ All changes saved', 'ok');
};

/* ── Inline edit mode ───────────────────────────────────────────────────── */
let _inlineActive = false;
window._toggleInlineEdit = function () { _inlineActive ? window._disableInlineEdit() : window._enableInlineEdit(); };
window._enableInlineEdit = function () {
  _inlineActive = true;
  document.querySelectorAll('[data-cms]').forEach(el => {
    if (el.tagName === 'IMG') {
      el.style.outline = '2px dashed var(--orange-500)';
      el.style.cursor  = 'pointer';
      el.title = 'Click to replace image';
      el.onclick = function () {
        const inp = document.createElement('input');
        inp.type = 'file'; inp.accept = 'image/*';
        inp.onchange = e => {
          const f = e.target.files[0]; if (!f) return;
          const r = new FileReader();
          r.onload = ev => { el.src = ev.target.result; window.CMS?.set(el.dataset.cms, ev.target.result); window.showToast?.('Image updated', 'ok'); };
          r.readAsDataURL(f);
        };
        inp.click();
      };
    } else {
      el.contentEditable = 'true';
      el.style.outline       = '2px dashed rgba(33,143,82,.4)';
      el.style.outlineOffset = '3px';
      el.style.borderRadius  = '3px';
      el.style.minHeight     = '1em';
      el.title = 'Click to edit';
      el.addEventListener('blur', _onEditBlur, { once: false });
    }
  });
  const tb = document.getElementById('cms-toolbar');
  if (tb) tb.style.display = 'flex';
};
window._disableInlineEdit = function () {
  _inlineActive = false;
  document.querySelectorAll('[data-cms]').forEach(el => {
    el.contentEditable = 'false';
    el.style.outline = ''; el.style.outlineOffset = ''; el.style.borderRadius = ''; el.style.cursor = ''; el.title = '';
    if (el.tagName === 'IMG') el.onclick = null;
    el.removeEventListener('blur', _onEditBlur);
  });
};
function _onEditBlur(e) {
  const el  = e.target;
  const key = el.dataset.cms;
  if (key) window.CMS?.set(key, el.innerText.trim());
}

/* ── FOOTER ──────────────────────────────────────────────────────────────── */
window.injectFooter = function () {
  const el = document.querySelector('.site-footer');
  if (!el) return;
  const cfg  = window.SITE_CONFIG || {};
  const name = cfg.ORG_NAME || 'THRIVE';
  el.innerHTML = `
    <footer class="footer" role="contentinfo">
      <div class="footer-grid">
        <div>
          <a href="index.html" aria-label="${name} — Home">${window.LOGO_HTML(true)}</a>
          <p class="footer-brand" data-cms="footer_tagline">
            Raising the next generation of champions through technology, sport, and community.
          </p>
          <div style="display:inline-flex;align-items:center;gap:5px;font-size:.7rem;color:rgba(255,255,255,.3);margin-top:10px">
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            Privacy-first · Minimal data
          </div>
        </div>
        <div>
          <div class="footer-hdr">Navigate</div>
          <ul class="footer-links">
            <li><a href="index.html"      class="footer-lnk">Home</a></li>
            <li><a href="about.html"      class="footer-lnk">About</a></li>
            <li><a href="activities.html" class="footer-lnk">Activities</a></li>
            <li><a href="gallery.html"    class="footer-lnk">Gallery</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-hdr">Programme</div>
          <ul class="footer-links">
            <li><a href="activities.html#tech"         class="footer-lnk">Tech Innovation</a></li>
            <li><a href="activities.html#league-hub"   class="footer-lnk">Football League</a></li>
            <li><a href="activities.html#tedtalk"      class="footer-lnk">Inspiration Talks</a></li>
            <li><a href="activities.html#quiz-hub"     class="footer-lnk">Quiz Arena</a></li>
            <li><a href="gallery.html"                 class="footer-lnk">Gallery & Videos</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-hdr">Support</div>
          <ul class="footer-links">
            <li><a href="donate.html"               class="footer-lnk">Donate / Sponsor</a></li>
            <li><a href="contact.html#volunteer"    class="footer-lnk">Volunteer</a></li>
            <li><a href="contact.html"              class="footer-lnk">Contact Us</a></li>
            <li><a href="privacy.html"              class="footer-lnk">Privacy Policy</a></li>
            <li><a href="terms.html"                class="footer-lnk">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-btm">
        <span class="footer-copy">
          © ${new Date().getFullYear()} <span data-org-name>${name}</span> ·
          Independent Youth Development Initiative · Nigeria
        </span>
        <span style="color:rgba(255,255,255,.25);font-size:.76rem;font-style:italic" data-cms="footer_quote">
          "Every living being is designed to grow and thrive."
        </span>
      </div>
    </footer>`;
};

/* ═══════════════════════════════════════════
   THRIVE — components.js
   Shared nav, footer, logo SVG
   ═══════════════════════════════════════════ */
'use strict';

/* ── LOGO LOCKUP ── image + wordmark side by side ── */
window.LOGO_SVG=function(dark){
  /* dark=true → use on dark nav/footer; false → use on light bg */
  const nameCol = dark ? '#FFFFFF' : '#1C2B1C';
  const tagCol  = dark ? '#3DB870' : '#1B7B78';
  const name    = (window.SITE_CONFIG&&window.SITE_CONFIG.ORG_NAME)||'TriveFoundation';
  const tagline = (window.SITE_CONFIG&&window.SITE_CONFIG.ORG_TAGLINE)||'Raising Champions';
  return `<span class="logo-lockup" aria-label="${name} — ${tagline}" role="img" style="display:inline-flex;align-items:center;gap:10px;text-decoration:none">
    <img src="assets/tree-logo.png" alt="" aria-hidden="true"
         style="height:52px;width:auto;object-fit:contain;flex-shrink:0">
    <span style="display:flex;flex-direction:column;line-height:1">
      <span data-org-name style="font-family:Georgia,'Times New Roman',serif;font-size:1.35rem;font-weight:700;letter-spacing:.08em;color:${nameCol}">${name}</span>
      <span style="font-family:'DM Sans',system-ui,sans-serif;font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:${tagCol};margin-top:2px">${tagline}</span>
    </span>
  </span>`;
};

/* ── NAV ── */
window.injectNav=function(){
  const el=document.querySelector('.nav');if(!el)return;
  const cfg=window.SITE_CONFIG||{};
  const name=cfg.ORG_NAME||'TriveFoundation';
  el.innerHTML=`<div class="nav-inner">
    <a href="index.html" class="nav-logo" aria-label="${name} — Home">${window.LOGO_SVG(true)}</a>
    <nav class="nav-links" role="navigation" aria-label="Main navigation">
      <a href="index.html" class="nav-link">Home</a>
      <a href="about.html" class="nav-link">About</a>
      <a href="activities.html" class="nav-link">Activities</a>
      <a href="gallery.html" class="nav-link">Gallery</a>
      <a href="contact.html" class="nav-link">Contact</a>
      <a href="donate.html" class="nav-link nav-donate-btn">Donate</a>
    </nav>
    <div style="display:flex;align-items:center;gap:8px;flex-shrink:0">
      <button id="nav-admin-btn" onclick="window._openAdminLogin()" aria-label="Admin login"
        style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.7);
               padding:6px 13px;border-radius:var(--r-sm);font-size:.78rem;font-weight:600;
               display:flex;align-items:center;gap:5px;cursor:pointer;transition:all var(--t)">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span id="nav-admin-lbl">Admin</span>
      </button>
      <button class="nav-hamburger" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>`;
  /* Hide admin button for external users; reveal for logged-in admins only */
  _setAdminNavState(Boolean(window.AdminAuth?.isLoggedIn()));
  document.dispatchEvent(new CustomEvent('thrive:nav-injected'));
};

function _setAdminNavState(on){
  const btn=document.getElementById('nav-admin-btn');
  const lbl=document.getElementById('nav-admin-lbl');
  if(!btn||!lbl)return;
  if(on){
    btn.style.display='flex';
    btn.style.background='rgba(46,125,79,.35)';
    btn.style.borderColor='rgba(61,214,140,.4)';
    btn.style.color='#3DB870';
    lbl.textContent='Edit Content';
  } else {
    btn.style.display='none';
    btn.style.background='rgba(255,255,255,.1)';
    btn.style.borderColor='rgba(255,255,255,.2)';
    btn.style.color='rgba(255,255,255,.7)';
    lbl.textContent='Admin';
  }
}

/* Inject the login modal + CMS panel once into every page */
window.injectAdminUI=function(){
  if(document.getElementById('_thrive-admin-ui'))return; /* only once */
  const wrap=document.createElement('div');
  wrap.id='_thrive-admin-ui';
  wrap.innerHTML=`
<!-- ── Admin login modal ── -->
<div id="login-modal" class="modal-bg" role="dialog" aria-modal="true" aria-labelledby="login-modal-title" style="display:none">
  <div class="modal-box" style="max-width:400px">
    <h2 id="login-modal-title" style="margin-bottom:.4rem;font-size:1.1rem">Admin Access</h2>
    <p style="font-size:.86rem;color:var(--c-muted);margin-bottom:1rem">Enter the admin PIN to manage content and results.</p>
    <div id="login-err" role="alert" style="display:none;background:#FEF2F2;border:1px solid #FECACA;border-radius:var(--r-sm);padding:8px 12px;font-size:.82rem;color:#DC2626;margin-bottom:10px"></div>
    <div class="fg" style="margin-bottom:14px">
      <label for="admin-pin-inp" style="font-size:.84rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:5px">PIN</label>
      <input type="password" id="admin-pin-inp" autocomplete="current-password" maxlength="20" placeholder="Enter admin PIN"
        style="width:100%;padding:10px 13px;border:1.5px solid var(--c-border);border-radius:var(--r-sm);font-size:.92rem;background:var(--c-cream)">
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn btn-green" onclick="window._doAdminLogin()">Sign In</button>
      <button class="btn" style="background:var(--c-sand);color:var(--c-muted)" onclick="window._closeLoginModal()">Cancel</button>
    </div>
    <p style="font-size:.74rem;color:var(--c-muted);margin-top:12px">PIN available to authorised administrators only</p>
  </div>
</div>

<!-- ── CMS editing toolbar (shown when logged in) ── -->
<div id="cms-toolbar" role="toolbar" aria-label="Content editor"
  style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:1200;
         background:rgba(19,45,31,.96);backdrop-filter:blur(16px);
         border-top:2px solid var(--c-green);
         padding:10px clamp(14px,4vw,40px);
         display:none;align-items:center;gap:10px;flex-wrap:wrap">
  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--c-green-lt)" stroke-width="2" aria-hidden="true"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
  <span style="color:rgba(255,255,255,.65);font-size:.82rem">Edit mode — click any highlighted text or image to edit</span>
  <button onclick="window._cmsSaveAll()" class="btn btn-green btn-sm">Save All Changes</button>
  <button onclick="window._openCMSPanel()" class="btn btn-sm" style="background:rgba(255,255,255,.1);color:#fff">Site Settings</button>
  <button onclick="window._adminLogout()" class="btn btn-sm" style="background:transparent;color:rgba(255,255,255,.45);border:1px solid rgba(255,255,255,.15)">Log Out</button>
</div>

<!-- ── CMS Settings panel (slide-up) ── -->
<div id="cms-panel-bg" style="display:none;position:fixed;inset:0;z-index:1300;background:rgba(0,0,0,.45)" onclick="if(event.target===this)window._closeCMSPanel()">
  <div id="cms-panel" role="dialog" aria-modal="true" aria-labelledby="cms-panel-title"
    style="position:absolute;bottom:0;left:0;right:0;background:var(--c-white);
           border-radius:var(--r-xl) var(--r-xl) 0 0;
           max-height:90svh;overflow-y:auto;padding:24px clamp(16px,4vw,40px) 40px">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px">
      <h2 id="cms-panel-title" style="font-size:1.15rem">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--c-teal)" stroke-width="2" style="vertical-align:middle;margin-right:6px"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
        Site Settings
      </h2>
      <button onclick="window._closeCMSPanel()" aria-label="Close" style="background:var(--c-sand);border:none;border-radius:50%;width:32px;height:32px;font-size:1.1rem;cursor:pointer;color:var(--c-muted)">✕</button>
    </div>

    <div class="cms-tab-bar" role="tablist" style="display:flex;gap:4px;border-bottom:1px solid var(--c-border);margin-bottom:20px;flex-wrap:wrap">
      <button class="cms-t active" onclick="cmsTab(0,this)" style="padding:8px 16px;border:none;background:none;font-weight:600;color:var(--c-teal);border-bottom:2px solid var(--c-teal);cursor:pointer;font-size:.85rem">Identity</button>
      <button class="cms-t" onclick="cmsTab(1,this)" style="padding:8px 16px;border:none;background:none;font-weight:600;color:var(--c-muted);border-bottom:2px solid transparent;cursor:pointer;font-size:.85rem">Homepage</button>
      <button class="cms-t" onclick="cmsTab(2,this)" style="padding:8px 16px;border:none;background:none;font-weight:600;color:var(--c-muted);border-bottom:2px solid transparent;cursor:pointer;font-size:.85rem">Stats</button>
      <button class="cms-t" onclick="cmsTab(3,this)" style="padding:8px 16px;border:none;background:none;font-weight:600;color:var(--c-muted);border-bottom:2px solid transparent;cursor:pointer;font-size:.85rem">Donate</button>
      <button class="cms-t" onclick="cmsTab(4,this)" style="padding:8px 16px;border:none;background:none;font-weight:600;color:var(--c-muted);border-bottom:2px solid transparent;cursor:pointer;font-size:.85rem">Footer</button>
    </div>

    <div id="cms-panels-wrap">
      <!-- Identity -->
      <div class="cms-panel active" style="display:block">
        <p style="font-size:.82rem;background:rgba(27,123,120,.08);border-radius:var(--r-sm);padding:10px 13px;color:var(--c-teal);margin-bottom:16px">Changing the name here updates it everywhere — nav, footer, all pages. Refresh other tabs to see it.</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px" class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Organisation Name</label><input id="cms-org-name" type="text" class="fi" placeholder="TriveFoundation"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Tagline</label><input id="cms-org-tagline" type="text" class="fi" placeholder="Raising Champions"></div>
        </div>
        <div style="margin-bottom:12px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Mission Statement</label><input id="cms-org-mission" type="text" class="fi"></div>
        <div style="margin-bottom:16px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Contact Email</label><input id="cms-org-email" type="email" class="fi"></div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('identity')">Save Identity</button>
      </div>

      <!-- Homepage -->
      <div class="cms-panel" style="display:none">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px" class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Hero Line 1</label><input id="cms-hero1" type="text" class="fi" placeholder="A Time"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Hero Line 2 (italic)</label><input id="cms-hero2" type="text" class="fi" placeholder="To Build"></div>
        </div>
        <div style="margin-bottom:12px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Hero Body Text</label><textarea id="cms-hero-body" rows="2" class="fi" style="resize:vertical"></textarea></div>
        <div style="margin-bottom:12px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Parallax Quote</label><textarea id="cms-hero-quote" rows="2" class="fi" style="resize:vertical"></textarea></div>
        <div style="margin-bottom:16px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Quote Attribution</label><input id="cms-quote-cite" type="text" class="fi"></div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('homepage')">Save Homepage</button>
      </div>

      <!-- Stats -->
      <div class="cms-panel" style="display:none">
        <p style="font-size:.82rem;color:var(--c-muted);margin-bottom:14px">These numbers animate on the homepage stats bar.</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px" class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Youth Trained (number)</label><input id="cms-stat-youth" type="number" min="0" class="fi"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Label</label><input id="cms-stat-youth-lbl" type="text" class="fi"></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px" class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Event Hours (number)</label><input id="cms-stat-hours" type="number" min="0" class="fi"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Label</label><input id="cms-stat-hours-lbl" type="text" class="fi"></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px" class="cms-field-row">
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Partners (number)</label><input id="cms-stat-partners" type="number" min="0" class="fi"></div>
          <div><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Label</label><input id="cms-stat-partners-lbl" type="text" class="fi"></div>
        </div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('stats')">Save Stats</button>
      </div>

      <!-- Donate -->
      <div class="cms-panel" style="display:none">
        <div style="margin-bottom:12px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Donate Page Title</label><input id="cms-donate-title" type="text" class="fi"></div>
        <div style="margin-bottom:12px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Donate Subtitle</label><textarea id="cms-donate-sub" rows="2" class="fi" style="resize:vertical"></textarea></div>
        <div style="margin-bottom:16px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Payment Reference Note</label><input id="cms-bank-confirm" type="text" class="fi"></div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('donate')">Save Donate</button>
      </div>

      <!-- Footer -->
      <div class="cms-panel" style="display:none">
        <div style="margin-bottom:12px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Footer Tagline</label><textarea id="cms-footer-tag" rows="2" class="fi" style="resize:vertical"></textarea></div>
        <div style="margin-bottom:16px"><label style="font-size:.82rem;font-weight:600;color:var(--c-dark);display:block;margin-bottom:4px">Footer Quote</label><input id="cms-footer-quote" type="text" class="fi"></div>
        <button class="btn btn-green btn-sm" onclick="saveCMS('footer')">Save Footer</button>
      </div>
    </div>
  </div>
</div>`;
  document.body.appendChild(wrap);


  /* Hidden shortcut for admins: Ctrl/Cmd + Shift + A opens admin login */
  if(!window._adminShortcutBound){
    window._adminShortcutBound=true;
    document.addEventListener('keydown',e=>{
      const aKey=String(e.key||'').toLowerCase()==='a';
      if(aKey&&(e.ctrlKey||e.metaKey)&&e.shiftKey){
        e.preventDefault();
        window._openAdminLogin();
      }
    });
  }

  /* Keyboard: Enter submits login */
  document.getElementById('admin-pin-inp')?.addEventListener('keydown',e=>{
    if(e.key==='Enter') window._doAdminLogin();
    if(e.key==='Escape') window._closeLoginModal();
  });
}; /* end injectAdminUI */

/* ── Global admin control functions (called from nav button + toolbar) ── */
window._openAdminLogin=function(){
  if(window.AdminAuth?.isLoggedIn()){
    /* Already in — toggle inline edit mode */
    window._toggleInlineEdit();
    return;
  }
  const m=document.getElementById('login-modal');
  if(m){m.style.display='flex';document.body.style.overflow='hidden';document.getElementById('admin-pin-inp')?.focus();}
};
window._closeLoginModal=function(){
  const m=document.getElementById('login-modal');
  if(m){m.style.display='none';document.body.style.overflow='';}
  document.getElementById('login-err').style.display='none';
  document.getElementById('admin-pin-inp').value='';
};
window._doAdminLogin=function(){
  if(window._locked()){_showLoginErr('Too many attempts. Wait 60 seconds.');return;}
  const pin=document.getElementById('admin-pin-inp')?.value||'';
  const result=window.AdminAuth?.login(pin);
  if(result===true){
    window._closeLoginModal();
    _setAdminNavState(true);
    document.getElementById('cms-toolbar').style.display='flex';
    window._enableInlineEdit();
    window.showToast?.('Admin mode active — click highlighted text or images to edit','ok');
    /* Show .admin-only sections on this page */
    document.querySelectorAll('.admin-only').forEach(el=>el.style.display='block');
    document.dispatchEvent(new CustomEvent('thrive:admin-state',{detail:{loggedIn:true}}));
  } else {
    _showLoginErr(window._locked()?'Locked — too many attempts. Wait 60s.':'Incorrect PIN.');
    document.getElementById('admin-pin-inp').value='';
  }
};
function _showLoginErr(msg){
  const e=document.getElementById('login-err');
  if(e){e.textContent=msg;e.style.display='block';}
}
window._adminLogout=function(){
  window.AdminAuth?.logout();
  _setAdminNavState(false);
  document.getElementById('cms-toolbar').style.display='none';
  window._disableInlineEdit();
  document.querySelectorAll('.admin-only').forEach(el=>el.style.display='none');
  document.dispatchEvent(new CustomEvent('thrive:admin-state',{detail:{loggedIn:false}}));
  window.showToast?.('Logged out');
};
window._openCMSPanel=function(){
  const bg=document.getElementById('cms-panel-bg');
  if(bg){bg.style.display='flex';document.body.style.overflow='hidden';}
  /* Pre-fill fields from stored CMS data */
  const d=window.CMS?._d||{};
  const cfg=window.SITE_CONFIG||{};
  _setVal('cms-org-name',    d.org_name||cfg.ORG_NAME||'');
  _setVal('cms-org-tagline', d.org_tagline||cfg.ORG_TAGLINE||'');
  _setVal('cms-org-mission', d.org_mission||cfg.ORG_MISSION||'');
  _setVal('cms-org-email',   d.org_email||cfg.ORG_EMAIL||'');
  _setVal('cms-hero1',       d.hero_line1||cfg.HERO_LINE1||'');
  _setVal('cms-hero2',       d.hero_line2||cfg.HERO_LINE2||'');
  _setVal('cms-hero-body',   d.hero_body||cfg.HERO_BODY||'');
  _setVal('cms-hero-quote',  d.hero_quote||'');
  _setVal('cms-quote-cite',  d.hero_quote_cite||'');
  const s=cfg.STATS||{};
  _setVal('cms-stat-youth',     d.stat_youth_count ??s.youth?.value??'');
  _setVal('cms-stat-youth-lbl', d.stat_youth_label ||s.youth?.label||'');
  _setVal('cms-stat-hours',     d.stat_hours_count ??s.hours?.value??'');
  _setVal('cms-stat-hours-lbl', d.stat_hours_label ||s.hours?.label||'');
  _setVal('cms-stat-partners',  d.stat_partners_count??s.partners?.value??'');
  _setVal('cms-stat-partners-lbl', d.stat_partners_label||s.partners?.label||'');
  _setVal('cms-donate-title',  d.donate_title||'');
  _setVal('cms-donate-sub',    d.donate_sub||'');
  _setVal('cms-bank-confirm',  d.bank_confirm||cfg.BANK?.note||'');
  _setVal('cms-footer-tag',    d.footer_tagline||'');
  _setVal('cms-footer-quote',  d.footer_quote||'');
};
function _setVal(id,val){const el=document.getElementById(id);if(el)el.value=val;}
window._closeCMSPanel=function(){
  const bg=document.getElementById('cms-panel-bg');
  if(bg){bg.style.display='none';document.body.style.overflow='';}
};

/* Tab switching inside CMS panel */
window.cmsTab=function(idx,btn){
  document.querySelectorAll('.cms-t').forEach((b,i)=>{
    b.classList.toggle('active',i===idx);
    b.style.color=i===idx?'var(--c-teal)':'var(--c-muted)';
    b.style.borderBottom=i===idx?'2px solid var(--c-teal)':'2px solid transparent';
  });
  document.querySelectorAll('#cms-panels-wrap .cms-panel').forEach((p,i)=>p.style.display=i===idx?'block':'none');
};

/* Save individual sections */
window.saveCMS=function(section){
  if(!window.CMS)return;
  const g=id=>document.getElementById(id)?.value?.trim()||'';
  if(section==='identity'){
    window.CMS.set('org_name',       g('cms-org-name'));
    window.CMS.set('org_tagline',    g('cms-org-tagline'));
    window.CMS.set('org_mission',    g('cms-org-mission'));
    window.CMS.set('org_email',      g('cms-org-email'));
    /* Live-update org name on page */
    const name=g('cms-org-name')||window.SITE_CONFIG?.ORG_NAME||'TriveFoundation';
    document.querySelectorAll('[data-org-name]').forEach(el=>el.textContent=name);
    document.title=document.title.replace(/TriveFoundation/g,name);
  }
  if(section==='homepage'){
    window.CMS.set('hero_line1',      g('cms-hero1'));
    window.CMS.set('hero_line2',      g('cms-hero2'));
    window.CMS.set('hero_body',       g('cms-hero-body'));
    window.CMS.set('hero_quote',      g('cms-hero-quote'));
    window.CMS.set('hero_quote_cite', g('cms-quote-cite'));
  }
  if(section==='stats'){
    window.CMS.set('stat_youth_count',       g('cms-stat-youth'));
    window.CMS.set('stat_youth_label',       g('cms-stat-youth-lbl'));
    window.CMS.set('stat_hours_count',       g('cms-stat-hours'));
    window.CMS.set('stat_hours_label',       g('cms-stat-hours-lbl'));
    window.CMS.set('stat_partners_count',    g('cms-stat-partners'));
    window.CMS.set('stat_partners_label',    g('cms-stat-partners-lbl'));
    /* Live update stat numbers and labels */
    const fields=[
      ['stat_youth_count','stat_youth_label','count-anim:first-child','stat-lbl:first-child'],
    ];
    // Simpler: just re-apply CMS and rely on page re-render
  }
  if(section==='donate'){
    window.CMS.set('donate_title',  g('cms-donate-title'));
    window.CMS.set('donate_sub',    g('cms-donate-sub'));
    window.CMS.set('bank_confirm',  g('cms-bank-confirm'));
  }
  if(section==='footer'){
    window.CMS.set('footer_tagline', g('cms-footer-tag'));
    window.CMS.set('footer_quote',   g('cms-footer-quote'));
    document.querySelectorAll('[data-cms="footer_tagline"]').forEach(el=>el.textContent=g('cms-footer-tag'));
    document.querySelectorAll('[data-cms="footer_quote"]').forEach(el=>el.textContent=g('cms-footer-quote'));
  }
  window.CMS.apply();
  window.showToast?.('✓ Saved','ok');
};

/* Save ALL inline edits at once */
window._cmsSaveAll=function(){
  document.querySelectorAll('[data-cms][contenteditable="true"]').forEach(el=>{
    window.CMS?.set(el.dataset.cms, el.innerText.trim());
  });
  window.showToast?.('✓ All changes saved','ok');
};

/* ── INLINE EDIT MODE ── */
let _inlineActive=false;
window._toggleInlineEdit=function(){
  _inlineActive?window._disableInlineEdit():window._enableInlineEdit();
};
window._enableInlineEdit=function(){
  _inlineActive=true;
  document.querySelectorAll('[data-cms]').forEach(el=>{
    if(el.tagName==='IMG'){
      /* Images: click to replace */
      el.style.outline='2px dashed var(--c-orange)';
      el.style.cursor='pointer';
      el.title='Click to replace image';
      el.onclick=function(){
        const inp=document.createElement('input');inp.type='file';inp.accept='image/*';
        inp.onchange=e=>{
          const f=e.target.files[0];if(!f)return;
          const r=new FileReader();
          r.onload=ev=>{el.src=ev.target.result;window.CMS?.set(el.dataset.cms,ev.target.result);window.showToast?.('Image updated','ok');};
          r.readAsDataURL(f);
        };inp.click();
      };
    } else {
      el.contentEditable='true';
      el.style.outline='2px dashed rgba(46,125,79,.45)';
      el.style.outlineOffset='3px';
      el.style.borderRadius='3px';
      el.style.minHeight='1em';
      el.title='Click to edit';
      el.addEventListener('blur',_onEditBlur,{once:false});
    }
  });
  document.getElementById('cms-toolbar').style.display='flex';
};
window._disableInlineEdit=function(){
  _inlineActive=false;
  document.querySelectorAll('[data-cms]').forEach(el=>{
    el.contentEditable='false';
    el.style.outline='';el.style.outlineOffset='';el.style.borderRadius='';el.style.cursor='';el.title='';
    if(el.tagName==='IMG') el.onclick=null;
    el.removeEventListener('blur',_onEditBlur);
  });
};
function _onEditBlur(e){
  const el=e.target;const key=el.dataset.cms;
  if(key) window.CMS?.set(key,el.innerText.trim());
}

/* ── FOOTER ── */
window.injectFooter=function(){
  const el=document.querySelector('.site-footer');if(!el)return;
  const cfg=window.SITE_CONFIG||{};
  const name=cfg.ORG_NAME||'TriveFoundation';
  el.innerHTML=`<footer class="footer" role="contentinfo">
    <div class="footer-grid">
      <div>
        <a href="index.html" aria-label="${name} — Home">${window.LOGO_SVG(true)}</a>
        <p class="footer-brand" data-cms="footer_tagline">Raising the next generation of champions through technology, sport, and community.</p>
        <div class="sec-badge">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Secure · No tracking · Privacy-first
        </div>
      </div>
      <div>
        <div class="footer-hdr">Navigate</div>
        <ul class="footer-links">
          <li><a href="index.html" class="footer-lnk">Home</a></li>
          <li><a href="about.html" class="footer-lnk">About</a></li>
          <li><a href="activities.html" class="footer-lnk">Activities</a></li>
          <li><a href="activities.html#league-hub" class="footer-lnk">League</a></li>
          <li><a href="activities.html#quiz-hub" class="footer-lnk">Quiz</a></li>
          <li><a href="gallery.html" class="footer-lnk">Gallery & Videos</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-hdr">Programme</div>
        <ul class="footer-links">
          <li><a href="activities.html#tech" class="footer-lnk">Tech Innovation</a></li>
          <li><a href="activities.html#league-hub" class="footer-lnk">Football League</a></li>
          <li><a href="activities.html#tedtalk" class="footer-lnk">Inspiration Talks</a></li>
          <li><a href="activities.html#quiz-hub" class="footer-lnk">Quiz Arena</a></li>
          <li><a href="gallery.html" class="footer-lnk">Gallery</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-hdr">Support</div>
        <ul class="footer-links">
          <li><a href="donate.html" class="footer-lnk">Donate / Sponsor</a></li>
          <li><a href="contact.html#volunteer" class="footer-lnk">Volunteer</a></li>
          <li><a href="contact.html" class="footer-lnk">Contact Us</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-btm">
      <span class="footer-copy">© 2026 <span data-org-name>${name}</span> · Independent Youth Development Initiative · Nigeria</span>
      <span style="color:rgba(255,255,255,.28);font-size:.76rem;font-style:italic" data-cms="footer_quote">"Every living being is designed to grow and thrive."</span>
    </div>
  </footer>`;
};

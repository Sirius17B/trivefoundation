/**
 * THRIVE SITE CONFIG  ·  v5
 * ════════════════════════════════════════════════
 * REBRAND: change ORG_NAME (and optionally ORG_SHORT, ORG_TAGLINE).
 * Every page reads from window.SITE_CONFIG — one edit changes everything.
 * ════════════════════════════════════════════════
 */
'use strict';

window.SITE_CONFIG = {

  /* ── IDENTITY ─────────────────────────────────────────────────────────────
     To rename: change ORG_NAME and ORG_SHORT. All nav, footer, titles,
     meta descriptions, and leaderboard labels update automatically.
  ──────────────────────────────────────────────────────────────────────── */
  ORG_NAME:      'THRIVE',
  ORG_SHORT:     'THRIVE',          // Used in tight spaces (mobile nav, badges)
  ORG_TAGLINE:   'Raising Champions',
  ORG_YEAR:      '2026',
  ORG_SEASON:    'A Time To Build',
  ORG_MISSION:   'Empowering youth through technology, sport, and inspiration.',
  ORG_EMAIL:     'hello@thrivefoundation.org',
  ORG_PHONE:     '+234 800 000 0000',
  ORG_VENUE_2025:'FGC NISE, Anambra State, Nigeria',

  /* ── BACKEND ENDPOINTS ─────────────────────────────────────────────────
     Leave blank for mailto fallback. In production:
       contact:            /.netlify/functions/contact
       donor_confirmation: /.netlify/functions/donor-confirmation
  ──────────────────────────────────────────────────────────────────────── */
  API: {
    contact:            '',
    donor_confirmation: '',
  },

  /* ── HERO ──────────────────────────────────────────────────────────────── */
  HERO_LINE1:    'A Time',
  HERO_LINE2:    'To Build',
  HERO_EYEBROW:  'Now Active · 2026 Season',
  HERO_BODY:     'Technology. Sport. Inspiration. Three pillars. One mission — equipping young Nigerians with the skills and character to change their world.',

  /* ── STATS ─────────────────────────────────────────────────────────────── */
  STATS: {
    youth:    { value: 120, label: 'Youth Trained',    suffix: '+' },
    hours:    { value: 48,  label: 'Event Hours',      suffix: ''  },
    partners: { value: 6,   label: 'Partners & Donors', suffix: ''  },
  },

  /* ── DONATION TIERS ─────────────────────────────────────────────────────── */
  DONATION_TIERS: [
    { label: 'Seed',    amount: '₦10,000',  desc: 'Materials for one student' },
    { label: 'Sapling', amount: '₦50,000',  desc: 'Sponsor a full tech session' },
    { label: 'Tree',    amount: '₦150,000', desc: 'Fund one event day', featured: true },
    { label: 'Forest',  amount: '₦400,000', desc: 'Sponsor a school edition' },
  ],

  /* ── BANK DETAILS ─────────────────────────────────────────────────────── */
  BANK: {
    account_name: 'THRIVE Foundation',
    bank:         'First Bank of Nigeria',
    account_no:   '3012345678',
    sort_code:    '011152003',
    note:         'Use your full name as the payment reference.',
  },

  /* ── GALLERY ─────────────────────────────────────────────────────────── */
  GALLERY: [
    { src:'https://images.unsplash.com/photo-1489824904134-891ab64532f1?w=700&q=75&auto=format&fit=crop', alt:'African boys competing in a football match', label:'Boys Final — competitive football in action', tag:'football' },
    { src:'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=700&q=75&auto=format&fit=crop', alt:'Group of African teenagers working together on computers', label:'Tech training — collaboration and learning', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1529390079861-591de354faf5?w=700&q=75&auto=format&fit=crop', alt:'African girls in sports kit playing football', label:'Girls League — passion and skill on display', tag:'football' },
    { src:'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=700&q=75&auto=format&fit=crop', alt:'Young African children running and playing football on a field', label:'Community football — every child gets to play', tag:'football' },
    { src:'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=700&q=75&auto=format&fit=crop', alt:'African teenage girl focused on her laptop', label:'Building real digital projects from scratch', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=700&q=75&auto=format&fit=crop', alt:'Students in a computer lab on programming projects', label:'Tech innovation week — code, create, build', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=700&q=75&auto=format&fit=crop', alt:'Diverse group of young people celebrating together', label:'Celebrating every champion — closing awards', tag:'community' },
    { src:'https://images.unsplash.com/photo-1559523161-0fc0d8b814b4?w=700&q=75&auto=format&fit=crop', alt:'Young people listening to an inspirational speaker', label:'TED-style talks — stories that ignite ambition', tag:'community' },
    { src:'https://images.unsplash.com/photo-1529686342540-1b43aec0df75?w=700&q=75&auto=format&fit=crop', alt:'Children playing football in an open outdoor space', label:'Football league matchday atmosphere', tag:'football' },
    { src:'https://images.unsplash.com/photo-1511578314322-379afb476865?w=700&q=75&auto=format&fit=crop', alt:'Speaker addressing a large audience on stage', label:'Inspiration at the closing ceremony', tag:'community' },
    { src:'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=700&q=75&auto=format&fit=crop', alt:'Young person working on a technology project', label:'Tech showcase — capstone project presentations', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1552664730-d307ca884978?w=700&q=75&auto=format&fit=crop', alt:'Group of young African people working as a team', label:'Teamwork and collaboration in every session', tag:'community' },
  ],

  /* ── STORIES / NEWS FEED ─────────────────────────────────────────────── */
  STORIES: [
    {
      id: 'story-2026-03',
      date: 'March 2026',
      headline: 'THRIVE 2026 Officially Announced — Expanding to Three Schools',
      category: 'Announcement',
      body: 'We are thrilled to announce that THRIVE 2026 will be expanding its reach to three schools across the FCT. Building on the success of our maiden edition, we are set to bring technology training, competitive football, and inspirational talks to even more young Nigerians this year. Registration for partner schools opens in April.',
      image: 'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'Group of young African students excited and celebrating',
      featured: true,
    },
    {
      id: 'story-2026-02',
      date: 'February 2026',
      headline: 'New Quiz Arena Launched — Tech and Football Challenges Available Now',
      category: 'Tech',
      body: 'THRIVE participants can now test their knowledge through our brand-new online Quiz Arena. Two categories are live: Tech Challenge and Football Arena. Top scores appear on the leaderboard.',
      image: 'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'African student focused on a laptop completing an online quiz',
      featured: false,
    },
    {
      id: 'story-2025-11',
      date: 'November 2025',
      headline: 'THRIVE 2025 Closes with Record Participation at FGC NISE',
      category: 'Event',
      body: 'The maiden edition of THRIVE concluded at FGC NISE, Anambra State. Students competed in the football league, presented tech capstone projects, and attended TED-style talks. SS3 Boys won the football final 4–3 against JSS3; SS2 Girls won 3–1.',
      image: 'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'Young African students celebrating at an award ceremony',
      featured: false,
    },
    {
      id: 'story-2025-10',
      date: 'October 2025',
      headline: 'Tech Capstone Week: Students Build Real Apps and Websites',
      category: 'Tech',
      body: 'Over five days of intensive learning, THRIVE participants designed, built, and presented their own digital products. Projects ranged from weather apps and school portals to recipe finders.',
      image: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'African students working on computers during tech training',
      featured: false,
    },
    {
      id: 'story-2025-09',
      date: 'September 2025',
      headline: 'Football League Kicks Off — 14 Teams Compete Across Boys and Girls Divisions',
      category: 'Football',
      body: 'The THRIVE 2025 football season opened with 14 teams. Every match was fiercely contested. The league ran for four weeks with results tracked live on this website.',
      image: 'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'Young African children competing in a football league match',
      featured: false,
    },
  ],

  /* ── QUIZ SETTINGS ─────────────────────────────────────────────────────── */
  QUIZ_SETTINGS: {
    passMark:         50,
    timePerQuestion:  30,   // seconds per question
    showExplanations: true,
    shuffleQuestions: true,
    shuffleOptions:   false,
  },

  /* ── TEAM ─────────────────────────────────────────────────────────────── */
  TEAM: [
    { name:'Chisom Okoye',       role:'Founder & Programme Director', color:'#1A3D2B', photo:'' },
    { name:'Odinaka Okoye',      role:'Football Coordinator',         color:'#E8621A', photo:'' },
    { name:'Yahnazo Basil',      role:'ICT & Tech Facilitator',       color:'#1B7B78', photo:'' },
    { name:'Chisom Mmaduabuchi', role:'Logistics',                    color:'#2E7D4F', photo:'' },
    { name:'Josemaria Nriagu',   role:'Tech Support & Speaker',       color:'#6D28D9', photo:'' },
    { name:'Thankgod Nnajieneh', role:'Financial Partner',            color:'#1E3A5F', photo:'' },
  ],

  /* ── HIGHLIGHTS CAROUSEL ──────────────────────────────────────────────── */
  HIGHLIGHTS: [
    { img:'https://images.unsplash.com/photo-1489824904134-891ab64532f1?w=600&q=70&auto=format&fit=crop', alt:'Young African boys playing competitive football', tag:'football', tagLabel:'Football', title:'Boys Final: SS3 beat JSS3 4–3 in a dramatic finale', date:'THRIVE 2025 Finals' },
    { img:'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=600&q=70&auto=format&fit=crop', alt:'African students learning on computers', tag:'tech', tagLabel:'Tech', title:'Students build real apps and websites from scratch', date:'Tech Innovation Week' },
    { img:'https://images.unsplash.com/photo-1529390079861-591de354faf5?w=600&q=70&auto=format&fit=crop', alt:'African girls playing football on a sunny field', tag:'football', tagLabel:'Football', title:'Girls Final: SS2 Girls win 3–1 against SS1 Girls', date:'THRIVE 2025 Finals' },
    { img:'https://images.unsplash.com/photo-1559523161-0fc0d8b814b4?w=600&q=70&auto=format&fit=crop', alt:'Speaker giving an inspiring talk on stage', tag:'community', tagLabel:'Community', title:'TED-style talks inspire hundreds of students', date:'Closing Ceremony' },
    { img:'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=600&q=70&auto=format&fit=crop', alt:'Young people celebrating an award ceremony', tag:'community', tagLabel:'Community', title:'Award ceremony — celebrating every champion', date:'THRIVE 2025 Closing' },
    { img:'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=600&q=70&auto=format&fit=crop', alt:'Young African student focused on a laptop', tag:'tech', tagLabel:'Tech', title:'Capstone projects showcased and evaluated', date:'Tech Showcase Day' },
  ],

  /* ── QUIZZES ─────────────────────────────────────────────────────────────
     Questions built to international secondary school curriculum standards.
     Tech: covers computing, ICT, programming fundamentals, digital literacy.
     Football: covers Laws of the Game (IFAB), tactics, history, Nigerian football.
  ──────────────────────────────────────────────────────────────────────── */
  QUIZZES: [], // populated by quiz-bank.js
};

/**
 * TriveFoundation SITE CONFIG  ·  config.js
 * ════════════════════════════════
 * RENAME the organisation → change ORG_NAME (and optionally ORG_TAGLINE).
 * Every page reads from window.SITE_CONFIG so one edit changes everything.
 * Admins can override most values live via the CMS panel (stored in window.storage).
 */
'use strict';

window.SITE_CONFIG = {

  /* ── IDENTITY ─────────────────────────────────────────
     Change ORG_NAME here to rename across the whole site.
  ──────────────────────────────────────────────────────*/
  ORG_NAME:      'TriveFoundation',
  ORG_TAGLINE:   'Raising Champions',
  ORG_YEAR:      '2026',
  ORG_SEASON:    'A Time To Build',
  ORG_MISSION:   'Empowering youth through technology, sport, and inspiration.',
  ORG_EMAIL:     'camplucens@gmail.com', /* working default — update from Admin → Site Settings → Identity once a standard org email exists */
  ORG_PHONE:     '+234 800 000 0000',
  /* NOTE: THRIVE is an independent organisation. Events held at partner venues. */
  ORG_VENUE_2025:'FGC NISE, Anambra State, Nigeria',

  /* ── HERO HEADLINE ─────────────────────────────────── */
  HERO_LINE1:    'A Time',
  HERO_LINE2:    'To Build',
  HERO_EYEBROW:  'Now Active · 2026 Season',
  HERO_BODY:     'Technology. Sport. Inspiration. Three pillars. One mission — equipping young Nigerians with the skills and character to change their world.',

  /* ── STATS ─────────────────────────────────────────── */
  STATS: {
    youth:    { value: 120,  label: 'Youth Trained',    suffix: '+' },
    hours:    { value: 48,   label: 'Event Hours',      suffix: '' },
    partners: { value: 6,    label: 'Partners & Donors', suffix: '' },
  },

  /* ── BACKEND ENDPOINTS ───────────────────────────────
     Leave blank for static/mailto fallback. In production, point these
     to HTTPS endpoints such as /.netlify/functions/contact and
     /.netlify/functions/donor-confirmation.
  ──────────────────────────────────────────────────── */
  API: {
    contact: '',
    donor_confirmation: '',
  },

  /* ── DONATION TIERS (shown inline on CTA click) ───── */
  DONATION_TIERS: [
    { label: 'Starter', amount: '₦1,000', desc: 'Support one learner resource' },
    { label: 'Builder', amount: '₦5,000', desc: 'Contribute to guided training sessions' },
    { label: 'Impact', amount: '₦12,500', desc: 'Support project build materials' },
    { label: 'Growth', amount: '₦27,000', desc: 'Help fund coaching and mentorship' },
  ],

  /* ── BANK DETAILS (/donate.html) ───────────────────── */
  BANK: {
    account_name: 'TRIVE CARE SERVICES',
    bank:         'Sterling Bank',
    account_no:   '0148347000',
    note:         'Use your full name as the payment reference.',
  },

  /* ── GALLERY IMAGES ─────────────────────────────────
     Add / remove objects to change the gallery.
     tag: 'football' | 'tech' | 'community'
     alt: descriptive text for screen readers
  ──────────────────────────────────────────────────── */
  GALLERY: [
    { src:'https://images.unsplash.com/photo-1489824904134-891ab64532f1?w=700&q=75&auto=format&fit=crop', alt:'African boys competing in a football match on a grass pitch', label:'Boys final — competitive football in action', tag:'football' },
    { src:'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=700&q=75&auto=format&fit=crop', alt:'Group of African teenagers working together on computers', label:'Tech training — collaboration and learning', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1529390079861-591de354faf5?w=700&q=75&auto=format&fit=crop', alt:'African girls in sports kit playing football outdoors', label:'Girls league — passion and skill on display', tag:'football' },
    { src:'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=700&q=75&auto=format&fit=crop&crop=center', alt:'Young African children running and playing football on a field', label:'Community football — every child gets to play', tag:'football' },
    { src:'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=700&q=75&auto=format&fit=crop', alt:'African teenage girl focused on her laptop screen', label:'Building real digital projects from scratch', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=700&q=75&auto=format&fit=crop', alt:'Students in a computer lab working on programming projects', label:'Tech innovation week — code, create, build', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=700&q=75&auto=format&fit=crop', alt:'Diverse group of young people smiling and celebrating together', label:'Celebrating every champion — closing awards', tag:'community' },
    { src:'https://images.unsplash.com/photo-1559523161-0fc0d8b814b4?w=700&q=75&auto=format&fit=crop', alt:'Audience of young people listening to an inspirational speaker on stage', label:'TED-style talks — stories that ignite ambition', tag:'community' },
    { src:'https://images.unsplash.com/photo-1529686342540-1b43aec0df75?w=700&q=75&auto=format&fit=crop', alt:'Children playing football in a wide open outdoor space', label:'Football league matchday atmosphere', tag:'football' },
    { src:'https://images.unsplash.com/photo-1511578314322-379afb476865?w=700&q=75&auto=format&fit=crop', alt:'Speaker addressing a large audience on stage', label:'Inspiration and leadership at the closing ceremony', tag:'community' },
    { src:'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=700&q=75&auto=format&fit=crop', alt:'Young person working on a technology or programming project', label:'Tech showcase — capstone project presentations', tag:'tech' },
    { src:'https://images.unsplash.com/photo-1552664730-d307ca884978?w=700&q=75&auto=format&fit=crop', alt:'Group of young African people working together as a team', label:'Teamwork and collaboration in every session', tag:'community' },
  ],

  /* ── STORIES / NEWS FEED ───────────────────────────────
     Appears on Activities page as a news feed.
     Newest entries should come FIRST in the array.
     Admin can manage these via the admin panel on activities.html.
     Fields: id (unique), date, headline, category, body, image (URL or ''), featured (bool)
  ──────────────────────────────────────────────────── */
  STORIES: [
    {
      id: 'story-2026-03',
      date: 'March 2026',
      headline: 'TriveFoundation 2026 Officially Announced — Expanding to Three Schools',
      category: 'Announcement',
      body: 'We are thrilled to announce that TriveFoundation 2026 will be expanding its reach to three schools across the FCT. Building on the success of our maiden edition, we are set to bring technology training, competitive football, and inspirational talks to even more young Nigerians this year. Registration for partner schools opens in April.',
      image: 'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'Group of young African students excited and celebrating',
      featured: true,
    },
    {
      id: 'story-2026-02',
      date: 'February 2026',
      headline: 'New Quiz Arena Launched — Tech and Football Challenges Available Now',
      category: 'Tech',
      body: 'TriveFoundation participants can now test their knowledge through our brand-new online Quiz Arena. Two categories are live: Tech Challenge (50 questions on programming, computers and digital skills) and Football Arena (50 questions on football rules, history and tactics). Top scores appear on the leaderboard. More quiz categories coming soon.',
      image: 'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'African student focused on a laptop completing an online quiz',
      featured: false,
    },
    {
      id: 'story-2025-11',
      date: 'November 2025',
      headline: 'TriveFoundation 2025 Closes with Record Participation at FGC NISE',
      category: 'Event',
      body: 'The maiden edition of TriveFoundation concluded at FGC NISE, Anambra State, with every programmatic objective met. Students competed in the football league, presented tech capstone projects, and attended TED-style inspiration talks at the closing ceremony. SS3 Boys clinched the football final 4–3 against JSS3, while SS2 Girls won the girls competition 3–1.',
      image: 'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'Young African students celebrating at an award ceremony',
      featured: false,
    },
    {
      id: 'story-2025-10',
      date: 'October 2025',
      headline: 'Tech Capstone Week: Students Build Real Apps and Websites',
      category: 'Tech',
      body: 'Over five days of intensive learning, TriveFoundation participants at FGC NISE designed, built, and presented their own digital products. Projects ranged from weather apps and school portals to recipe finders and budget trackers. Facilitator Yahnazo Basil described the energy as "electric — these students exceeded every expectation."',
      image: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'African students working on computers during a tech training session',
      featured: false,
    },
    {
      id: 'story-2025-09',
      date: 'September 2025',
      headline: 'Football League Kicks Off — 14 Teams Compete Across Boys and Girls Divisions',
      category: 'Football',
      body: 'The TriveFoundation 2025 football season opened with 14 teams — 8 in the boys division and 6 in the girls division. Every match was fiercely contested. Football Coordinator Odinaka Okoye noted the remarkable level of organisation and sportsmanship from all participants. The league ran for four weeks, with results tracked live on this website.',
      image: 'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800&q=75&auto=format&fit=crop&crop=center',
      imageAlt: 'Young African children competing in a football league match',
      featured: false,
    },
  ],

  /* ── QUIZ SETTINGS ─────────────────────────────────
     passMark: minimum % to show "Pass"
     timePerQuestion: seconds per question (timer = questions × timePerQuestion)
     showExplanations: show answer explanation after each question
     shuffleQuestions: randomise order
  ──────────────────────────────────────────────────── */
  QUIZ_SETTINGS: {
    passMark:          50,
    timePerQuestion:   14,   /* seconds — 50 questions × 14s = ~12 min */
    showExplanations:  true,
    shuffleQuestions:  true,
    shuffleOptions:    false,
  },

  /* QUIZZES is intentionally NOT defined here — js/quiz-bank.js sets
     window.SITE_CONFIG.QUIZZES directly with the real, curated question
     bank (373 tech + 159 football). quiz-bank.js must load AFTER this
     file and BEFORE any page script reads SITE_CONFIG.QUIZZES. */

  TEAM: [
    { name:'Chisom Okoye',       role:'Founder & Programme Director', color:'#0A3D2E', photo:'https://images.unsplash.com/photo-1531384441138-2736e62e0919?w=200&q=80&auto=format&fit=crop&crop=faces' },
    { name:'Odinaka Okoye',      role:'Football Coordinator',         color:'#F97316', photo:'' },
    { name:'Yahnazo Basil',      role:'ICT & Tech Facilitator',       color:'#2D9E6B', photo:'' },
    { name:'Chisom Mmaduabuchi', role:'Logistics',                    color:'#0D7B7B', photo:'' },
    { name:'Josemaria Nriagu',   role:'Tech Support · TED Talk Speaker', color:'#7C3AED', photo:'' },
    { name:'Thankgod Nnajieneh', role:'Financial Partner',            color:'#1E3A5F', photo:'' },
  ],

  /* ── HIGHLIGHTS CAROUSEL ────────────────────────────── */
  HIGHLIGHTS: [
    { img:'https://images.unsplash.com/photo-1489824904134-891ab64532f1?w=600&q=70&auto=format&fit=crop', alt:'Young African boys playing competitive football on a grass pitch', tag:'football', tagLabel:'Football', title:'Boys Final: SS3 beat JSS 4–3 in a dramatic finale',   date:'TriveFoundation 2025 Finals' },
    { img:'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=600&q=70&auto=format&fit=crop', alt:'African students learning and working together on computers', tag:'tech',     tagLabel:'Tech',     title:'Students build real apps and websites from scratch',   date:'Tech Innovation Week' },
    { img:'https://images.unsplash.com/photo-1529390079861-591de354faf5?w=600&q=70&auto=format&fit=crop', alt:'African girls playing football on a sunny field', tag:'football', tagLabel:'Football', title:'Girls Final: SS2 Girls win 3–1 against SS1 Girls',     date:'TriveFoundation 2025 Finals' },
    { img:'https://images.unsplash.com/photo-1559523161-0fc0d8b814b4?w=600&q=70&auto=format&fit=crop', alt:'Speaker giving an inspiring TED-style talk on stage', tag:'community', tagLabel:'Community', title:'TED-style talks inspire hundreds of students',          date:'TriveFoundation Closing Ceremony' },
    { img:'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=600&q=70&auto=format&fit=crop', alt:'Diverse group of young people celebrating an award ceremony', tag:'community', tagLabel:'Community', title:'Award ceremony — celebrating every champion',           date:'TriveFoundation 2025 Closing' },
    { img:'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=600&q=70&auto=format&fit=crop', alt:'Young African student focused on a laptop screen', tag:'tech',     tagLabel:'Tech',     title:'Capstone projects showcased and evaluated',             date:'Tech Showcase Day' },
  ],
};

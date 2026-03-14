/**
 * THRIVE SITE CONFIG  ·  config.js
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
  ORG_NAME:      'THRIVE',
  ORG_TAGLINE:   'Raising Champions',
  ORG_YEAR:      '2026',
  ORG_SEASON:    'A Time To Build',
  ORG_MISSION:   'Empowering youth through technology, sport, and inspiration.',
  ORG_EMAIL:     'hello@thriveng.org',
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

  /* ── DONATION TIERS (shown inline on CTA click) ───── */
  DONATION_TIERS: [
    { label: 'Seed',     amount: '₦10,000',  desc: 'Materials for one student' },
    { label: 'Sapling',  amount: '₦50,000',  desc: 'Sponsor a full tech session' },
    { label: 'Tree',     amount: '₦150,000', desc: 'Fund one event day', featured: true },
    { label: 'Forest',   amount: '₦400,000', desc: 'Sponsor a school edition' },
  ],

  /* ── BANK DETAILS (/donate.html) ───────────────────── */
  BANK: {
    account_name: 'THRIVE Foundation',
    bank:         'First Bank of Nigeria',
    account_no:   '3012345678',
    sort_code:    '011152003',
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
      body: 'THRIVE participants can now test their knowledge through our brand-new online Quiz Arena. Two categories are live: Tech Challenge (50 questions on programming, computers and digital skills) and Football Arena (50 questions on football rules, history and tactics). Top scores appear on the leaderboard. More quiz categories coming soon.',
      image: 'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'African student focused on a laptop completing an online quiz',
      featured: false,
    },
    {
      id: 'story-2025-11',
      date: 'November 2025',
      headline: 'THRIVE 2025 Closes with Record Participation at FGC NISE',
      category: 'Event',
      body: 'The maiden edition of THRIVE concluded at FGC NISE, Anambra State, with every programmatic objective met. Students competed in the football league, presented tech capstone projects, and attended TED-style inspiration talks at the closing ceremony. SS3 Boys clinched the football final 4–3 against JSS3, while SS2 Girls won the girls competition 3–1.',
      image: 'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'Young African students celebrating at an award ceremony',
      featured: false,
    },
    {
      id: 'story-2025-10',
      date: 'October 2025',
      headline: 'Tech Capstone Week: Students Build Real Apps and Websites',
      category: 'Tech',
      body: 'Over five days of intensive learning, THRIVE participants at FGC NISE designed, built, and presented their own digital products. Projects ranged from weather apps and school portals to recipe finders and budget trackers. Facilitator Yahnazo Basil described the energy as "electric — these students exceeded every expectation."',
      image: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800&q=75&auto=format&fit=crop',
      imageAlt: 'African students working on computers during a tech training session',
      featured: false,
    },
    {
      id: 'story-2025-09',
      date: 'September 2025',
      headline: 'Football League Kicks Off — 14 Teams Compete Across Boys and Girls Divisions',
      category: 'Football',
      body: 'The THRIVE 2025 football season opened with 14 teams — 8 in the boys division and 6 in the girls division. Every match was fiercely contested. Football Coordinator Odinaka Okoye noted the remarkable level of organisation and sportsmanship from all participants. The league ran for four weeks, with results tracked live on this website.',
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

  QUIZZES: [
    {
      id: 'tech-general',
      title: 'Tech Challenge',
      category: 'tech',
      description: 'Test your knowledge of computers, programming, and digital technology.',
      questions: [
        { q:'What does HTML stand for?', options:['HyperText Markup Language','High-Tech Modern Language','HyperText Machine Learning','HyperLink Text Method'], answer:0, explanation:'HTML is the standard language used to create web pages.' },
        { q:'Which of these is a programming language?', options:['Google','Python','Chrome','Windows'], answer:1, explanation:'Python is a popular general-purpose programming language.' },
        { q:'What does CPU stand for?', options:['Central Power Unit','Computer Personal Unit','Central Processing Unit','Control Processing Unit'], answer:2, explanation:'The CPU (Central Processing Unit) is the brain of a computer.' },
        { q:'What does "www" stand for in a web address?', options:['World Wide Web','World Web Works','Wide World Web','Web Wide World'], answer:0 },
        { q:'Which device stores data permanently?', options:['RAM','CPU','Hard Disk Drive','Monitor'], answer:2, explanation:'Hard drives retain data even when the computer is switched off.' },
        { q:'What is a "bug" in programming?', options:['A type of computer virus','An error or flaw in code','A security password','A type of printer'], answer:1 },
        { q:'What does Wi-Fi allow you to do?', options:['Watch TV without a screen','Connect to the internet wirelessly','Print documents','Charge your phone'], answer:1 },
        { q:'Which of these is NOT a web browser?', options:['Chrome','Firefox','Safari','Photoshop'], answer:3, explanation:'Photoshop is image editing software, not a web browser.' },
        { q:'What does "AI" stand for?', options:['Automatic Interface','Artificial Intelligence','Advanced Internet','Automated Information'], answer:1 },
        { q:'What is the internet?', options:['A single computer','A type of software','A global network of connected computers','A storage device'], answer:2 },
        { q:'Which language is primarily used to style web pages?', options:['Java','CSS','Python','SQL'], answer:1, explanation:'CSS (Cascading Style Sheets) controls the visual appearance of web pages.' },
        { q:'What does "URL" stand for?', options:['Universal Resource Locator','Uniform Resource Locator','United Resource Link','Universal Resource Link'], answer:1 },
        { q:'What is a "server" in computing?', options:['A person who serves food','A computer that provides data to other computers','A type of keyboard','A printer model'], answer:1 },
        { q:'Which company created the Android operating system?', options:['Apple','Microsoft','Google','Samsung'], answer:2, explanation:'Android was developed by Google and is now the most widely used mobile OS.' },
        { q:'What does RAM stand for?', options:['Random Access Memory','Read-only Accessible Memory','Rapid Action Module','Remote Access Manager'], answer:0 },
        { q:'What is a "database"?', options:['A type of computer game','An organised collection of structured data','A kind of keyboard shortcut','A website template'], answer:1 },
        { q:'What does "HTTP" stand for?', options:['HyperText Transfer Protocol','High Traffic Transfer Program','HyperText Technology Protocol','Home Transfer Text Protocol'], answer:0 },
        { q:'What is "open source" software?', options:['Software that is always free to use','Software whose source code is publicly available','Software made by a single developer','Software with no security features'], answer:1 },
        { q:'Which of these is an example of an operating system?', options:['Microsoft Word','Google Chrome','Windows 11','Minecraft'], answer:2, explanation:'Windows 11 is an OS. Word and Chrome are applications that run on an OS.' },
        { q:'What does "encryption" do?', options:['Speeds up a computer','Converts data into a coded form to protect it','Deletes unwanted files','Connects to the internet'], answer:1 },
        { q:'What is the function of a "router" in networking?', options:['To display images','To direct data packets between computer networks','To store files','To power the computer'], answer:1 },
        { q:'What is "cloud computing"?', options:['Using weather data in software','Storing and accessing data/programs over the internet','A type of graphics processing','Building software for aircraft'], answer:1 },
        { q:'What programming concept means "repeating a block of code multiple times"?', options:['A function','A loop','A variable','A comment'], answer:1, explanation:'Loops (for/while) repeat instructions until a condition is met.' },
        { q:'What does "debugging" mean in programming?', options:['Adding new features to software','Finding and fixing errors in code','Deleting old files','Writing documentation'], answer:1 },
        { q:'What is an "algorithm"?', options:['A type of computer virus','A step-by-step procedure to solve a problem','A social media platform','A programming language'], answer:1 },
        { q:'What is "binary code"?', options:['A code used by spies','A number system using only 0s and 1s','A type of image file','A virus detection system'], answer:1, explanation:'All computer data is ultimately stored and processed as binary (0s and 1s).' },
        { q:'What does a "variable" store in programming?', options:['A fixed unchangeable value','A piece of data that can change during execution','The speed of the program','A type of loop'], answer:1 },
        { q:'What is "phishing" in cybersecurity?', options:['A type of computer game','A technique to trick users into revealing sensitive information','A method of fast file transfer','A way to speed up downloads'], answer:1 },
        { q:'What does "USB" stand for?', options:['Universal Serial Bus','United System Board','Universal Software Base','Unified Storage Bridge'], answer:0 },
        { q:'Which of these is a spreadsheet application?', options:['PowerPoint','Word','Excel','Outlook'], answer:2, explanation:'Microsoft Excel is a spreadsheet application used for data and calculations.' },
        { q:'What is "syntax" in programming?', options:['The speed at which code runs','The rules that define the structure of a programming language','A type of database','A security protocol'], answer:1 },
        { q:'What does "bandwidth" refer to in networking?', options:['The physical width of a cable','The maximum rate of data transfer across a network','The number of connected devices','The age of the network equipment'], answer:1 },
        { q:'What is a "function" in programming?', options:['A type of error','A reusable block of code that performs a specific task','A computer port','A file storage system'], answer:1 },
        { q:'Which file extension is commonly used for web pages?', options:['.docx','.html','.mp3','.xlsx'], answer:1, explanation:'.html files are the building blocks of web pages.' },
        { q:'What is "version control" in software development?', options:['Checking which Windows version you have','A system that tracks changes to code over time','Setting the screen resolution','Controlling user access levels'], answer:1, explanation:'Git is the most popular version control system.' },
        { q:'What does "API" stand for?', options:['Application Programming Interface','Automated Process Integration','Advanced Program Installer','Application Port Index'], answer:0, explanation:'APIs allow different software applications to communicate with each other.' },
        { q:'What is "machine learning"?', options:['Training people to use machines','A type of AI where systems learn from data without explicit programming','A method of computer maintenance','A game development framework'], answer:1 },
        { q:'What is a "pixel"?', options:['A unit of data storage','The smallest unit of a digital image','A type of network cable','A programming loop'], answer:1 },
        { q:'What does "LAN" stand for?', options:['Large Area Network','Local Access Node','Local Area Network','Long-range Access Network'], answer:2 },
        { q:'Which of the following is a cybersecurity best practice?', options:['Using the same password everywhere for convenience','Sharing your password with a trusted friend','Using a unique strong password for each account','Writing passwords on sticky notes near your computer'], answer:2 },
        { q:'What is "responsive design" in web development?', options:['A website that responds to user comments','A design that adapts to different screen sizes and devices','A very fast-loading website','A website with animated elements'], answer:1 },
        { q:'What is a "compiler" in programming?', options:['A person who writes code','A program that translates source code into machine code','A type of database','A debugging tool'], answer:1 },
        { q:'What does "IP address" identify?', options:['The speed of your internet connection','A unique device or host on a computer network','The brand of your router','The version of your browser'], answer:1 },
        { q:'What is "social engineering" in cybersecurity?', options:['Building social media apps','Manipulating people into revealing confidential information','Designing user interfaces','Managing social media accounts'], answer:1 },
        { q:'What is the purpose of a "firewall"?', options:['To speed up internet connections','To monitor and control incoming and outgoing network traffic based on rules','To store website data','To compress files'], answer:1 },
        { q:'What language is used to query databases?', options:['HTML','Python','SQL','JavaScript'], answer:2, explanation:'SQL (Structured Query Language) is used to communicate with databases.' },
        { q:'What is "boolean" in programming?', options:['A type of loop','A data type that is either true or false','A kind of function','A network protocol'], answer:1 },
        { q:'What does "IoT" stand for?', options:['Internet of Technology','Internet of Things','Integrated Operating Technology','Index of Tools'], answer:1, explanation:'IoT refers to everyday objects connected to the internet.' },
        { q:'What is "pseudocode"?', options:['Fake or broken code','An informal description of an algorithm in plain language','A type of encrypted code','A programming language for beginners'], answer:1 },
        { q:'What is the role of a "web server"?', options:['To browse websites','To store and serve web pages to clients over the internet','To create web designs','To write HTML code'], answer:1 },
      ],
    },
    {
      id: 'football-general',
      title: 'Football Arena',
      category: 'football',
      description: 'How well do you know the beautiful game? Rules, tactics, and history.',
      questions: [
        { q:'How many players are on a football team on the pitch?', options:['9','10','11','12'], answer:2 },
        { q:'How long is a standard football match?', options:['60 minutes','80 minutes','90 minutes','100 minutes'], answer:2 },
        { q:'What is awarded when a player is fouled inside the penalty area?', options:['Free kick','Corner kick','Penalty kick','Goal kick'], answer:2 },
        { q:'What does a yellow card mean?', options:['A goal is awarded','A warning to the player','The player is immediately sent off','A penalty kick is given'], answer:1 },
        { q:'How many points does a team get for a league win?', options:['1','2','3','4'], answer:2 },
        { q:'What position defends in front of the goal?', options:['Striker','Midfielder','Centre-back','Goalkeeper'], answer:3 },
        { q:'What is it called when a player scores three goals in one game?', options:['Hat-trick','Triple score','Three-peat','Goal rush'], answer:0 },
        { q:'Which country has won the most FIFA World Cups?', options:['Germany','Argentina','Brazil','France'], answer:2, explanation:'Brazil has won 5 FIFA World Cups: 1958, 1962, 1970, 1994, and 2002.' },
        { q:'What happens after 90 minutes in a knockout game if scores are level?', options:['The game is abandoned','Extra time is played','The home team wins automatically','A coin toss decides'], answer:1 },
        { q:'A corner kick is awarded when the ball goes out of play over the goal line and was last touched by whom?', options:['An attacking player','A defending player','The goalkeeper','The referee'], answer:1 },
        { q:'How long is each half of extra time in football?', options:['10 minutes','15 minutes','20 minutes','30 minutes'], answer:1 },
        { q:'What is the "offside rule" about?', options:['Running too fast','Being behind the second-last defender when the ball is played','Standing outside the pitch','Tackling from behind'], answer:1 },
        { q:'What is a "penalty shootout" used for?', options:['Practising penalties in training','Deciding the winner of a drawn knockout match','Punishing a player for misconduct','Ending a match early due to weather'], answer:1 },
        { q:'How wide is a standard football goal (in metres)?', options:['5.5m','6.5m','7.32m','8m'], answer:2, explanation:'A standard football goal is 7.32 metres wide and 2.44 metres tall.' },
        { q:'What does a red card mean?', options:['The player receives a warning','The player is substituted','The player is sent off and cannot return','A penalty is awarded'], answer:2 },
        { q:'What is a "free kick"?', options:['A kick given to restart play after a foul','A kick with no goalkeeper present','A kick from the centre circle','A kick that scores automatically'], answer:0 },
        { q:'What organisation governs world football?', options:['UEFA','CAF','FIFA','FA'], answer:2, explanation:'FIFA (Fédération Internationale de Football Association) governs world football.' },
        { q:'A goal kick is taken when the ball goes out over the goal line last touched by whom?', options:['A defending player','An attacking player','The goalkeeper','The referee'], answer:1 },
        { q:'How many substitutes are typically allowed in a standard football match?', options:['3','4','5','6'], answer:2, explanation:'Most competitions allow 5 substitutions in a match.' },
        { q:'What position plays between the defenders and attackers?', options:['Goalkeeper','Left winger','Midfielder','Striker'], answer:2 },
        { q:'What is "dribbling" in football?', options:['Passing the ball over long distances','Moving with the ball while maintaining close control','Shooting from distance','Heading the ball'], answer:1 },
        { q:'Which African country first reached a FIFA World Cup semi-final?', options:['Nigeria','Cameroon','Senegal','Ghana'], answer:1, explanation:'Cameroon reached the quarter-finals in 1990. No African team has reached the semi-finals.' },
        { q:'What is a "clean sheet"?', options:['A yellow card','When a goalkeeper concedes no goals in a match','A team winning by five goals','A new contract for a player'], answer:1 },
        { q:'What does "CAF" stand for in African football?', options:['Central African Federation','Confederation of African Football','Council of African Football','Continental African Federation'], answer:1 },
        { q:'What is a "through ball"?', options:['A ball kicked directly at the goalkeeper','A pass played between or behind defenders into space for an attacker','A long diagonal cross','A back-pass to the keeper'], answer:1 },
        { q:'How many officials typically oversee a professional football match?', options:['2','3','4','5'], answer:3, explanation:'A referee, two assistant referees, and a fourth official — typically four.' },
        { q:'What is the "AFCON"?', options:['African Football Cup of Notables','Africa Cup of Nations','African Football Confederation of Nations','Association for Continental Football'], answer:1, explanation:'AFCON is the Africa Cup of Nations, the main international football tournament in Africa.' },
        { q:'What does "possession" percentage measure in football?', options:['How many goals a team scores','The proportion of time a team has the ball','How fast a team runs','The number of fouls committed'], answer:1 },
        { q:'What is a "counter-attack"?', options:['Defending with many players behind the ball','A rapid attack launched after winning the ball from the opposition','A set piece from a corner','An attack down the wings'], answer:1 },
        { q:'What happens when the goalkeeper handles the ball outside the penalty area?', options:['Nothing','A penalty is awarded','A direct free kick is awarded to the opposition','The goal is disallowed'], answer:2 },
        { q:'What is a "brace" in football terms?', options:['When a player is injured','When a player scores two goals in one match','When a match ends 0-0','A type of defensive formation'], answer:1 },
        { q:'What does VAR stand for?', options:['Video Assisted Refereeing','Virtual Action Replay','Video Action Review','Variable Angle Refereeing'], answer:0, explanation:'VAR (Video Assistant Referee) uses video review to check key match decisions.' },
        { q:'Which position is sometimes referred to as a "sweeper"?', options:['Striker','Attacking midfielder','Libero/central defender behind the main defensive line','Winger'], answer:2 },
        { q:'What is the "Golden Boot" awarded for?', options:['Best goalkeeper in a tournament','Top scorer in a tournament','Best player in a tournament','Best young player in a tournament'], answer:1 },
        { q:'In a 4-4-2 formation, what do the numbers represent?', options:['Players on each wing','Defenders, Midfielders, Forwards','Shots, passes, goals','Speed, strength, stamina'], answer:1, explanation:'4-4-2 means 4 defenders, 4 midfielders, 2 forwards.' },
        { q:'What is "total football" (totaalvoetbal)?', options:['A system where every player can score','A tactical system where any outfield player can take over any position','Playing with the maximum number of attackers','A defensive system with all players behind the ball'], answer:1, explanation:'Total football was popularised by the Netherlands and Johan Cruyff in the 1970s.' },
        { q:'What is the "away goals rule" (when in use)?', options:['Goals scored away from home count double in a draw after two legs','Away teams get an extra goal advantage','Away goals are worth three points','Away teams shoot penalties first'], answer:0 },
        { q:'What Nigerian club is known as the "Pride of Rivers"?', options:['Kano Pillars','Enyimba','Rivers United','Shooting Stars'], answer:2 },
        { q:'What is "pressing" as a football tactic?', options:['Shooting from long range','Aggressively closing down opponents to win the ball back quickly','Playing a physical style of defence','Crossing from wide positions'], answer:1 },
        { q:'Which country hosts the Copa América?', options:['Spain','South American nations on rotation','Mexico','USA'], answer:1, explanation:'Copa América is hosted by South American nations and is the oldest international football tournament.' },
        { q:'What does a "nil-nil draw" mean?', options:['Both teams scored one goal','The match ended 0-0','The match was abandoned','Extra time was played'], answer:1 },
        { q:'What is the "box" in football?', options:['The dugout area','The penalty area','The centre circle','The technical area'], answer:1 },
        { q:'What year was the first FIFA World Cup held?', options:['1924','1930','1934','1938'], answer:1, explanation:'The first FIFA World Cup was held in Uruguay in 1930.' },
        { q:'What is "injury time" also called?', options:['Bonus time','Added time or stoppage time','Overtime','Recovery time'], answer:1 },
        { q:'How many players are in a team during a penalty shootout?', options:['Only goalkeepers','All players can take penalties','Any player on the pitch at the end of extra time','Only substitutes'], answer:2 },
        { q:'What is the Super Eagles?', options:['A South African club team','The Nigerian national football team','A Ghanaian club','A CAF competition'], answer:1, explanation:'The Super Eagles is the nickname of the Nigerian national football team.' },
        { q:'What does it mean to "nutmeg" an opponent?', options:['To tackle them hard','To pass the ball through their legs','To trick them with a feint','To score a long-range goal'], answer:1 },
        { q:'What is a "wall" in football?', options:['The advertising boards around the pitch','A line of defending players standing in front of a free kick','The goal frame','The barrier between fans and the pitch'], answer:1 },
        { q:'What is the Champions League?', options:['A Nigerian domestic competition','UEFA\'s premier European club competition','A World Cup qualifier','An African club competition'], answer:1 },
        { q:'What does "aggregate score" mean in a two-legged tie?', options:['The score after penalties','The combined total of goals scored across both matches','The number of yellow cards','The total possession across both games'], answer:1 },
        { q:'Who are traditionally considered the "Big 6" of English football?', options:['Arsenal, Chelsea, Liverpool, Man City, Man United, Tottenham','Arsenal, Chelsea, Everton, Liverpool, Man United, Newcastle','Arsenal, Chelsea, Liverpool, Leeds, Man City, Tottenham','Arsenal, Chelsea, Liverpool, Man City, Man United, Leicester'], answer:0 },
      ],
    },
  ],


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
    { img:'https://images.unsplash.com/photo-1489824904134-891ab64532f1?w=600&q=70&auto=format&fit=crop', alt:'Young African boys playing competitive football on a grass pitch', tag:'football', tagLabel:'Football', title:'Boys Final: SS3 beat JSS 4–3 in a dramatic finale',   date:'THRIVE 2025 Finals' },
    { img:'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=600&q=70&auto=format&fit=crop', alt:'African students learning and working together on computers', tag:'tech',     tagLabel:'Tech',     title:'Students build real apps and websites from scratch',   date:'Tech Innovation Week' },
    { img:'https://images.unsplash.com/photo-1529390079861-591de354faf5?w=600&q=70&auto=format&fit=crop', alt:'African girls playing football on a sunny field', tag:'football', tagLabel:'Football', title:'Girls Final: SS2 Girls win 3–1 against SS1 Girls',     date:'THRIVE 2025 Finals' },
    { img:'https://images.unsplash.com/photo-1559523161-0fc0d8b814b4?w=600&q=70&auto=format&fit=crop', alt:'Speaker giving an inspiring TED-style talk on stage', tag:'community', tagLabel:'Community', title:'TED-style talks inspire hundreds of students',          date:'THRIVE Closing Ceremony' },
    { img:'https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=600&q=70&auto=format&fit=crop', alt:'Diverse group of young people celebrating an award ceremony', tag:'community', tagLabel:'Community', title:'Award ceremony — celebrating every champion',           date:'THRIVE 2025 Closing' },
    { img:'https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?w=600&q=70&auto=format&fit=crop', alt:'Young African student focused on a laptop screen', tag:'tech',     tagLabel:'Tech',     title:'Capstone projects showcased and evaluated',             date:'Tech Showcase Day' },
  ],
};

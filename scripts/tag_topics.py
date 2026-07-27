#!/usr/bin/env python3
"""One-off script: adds a topic:'...' field to every question object in
js/quiz-bank.js, classified by keyword scoring against the question+options+
explanation text. Run once, then delete (or keep for future re-classification
if the bank grows). See memory: quiz-content-followup item #7."""
import re

PATH = 'js/quiz-bank.js'

with open(PATH, encoding='utf-8') as f:
    src = f.read()

# Split into lines, find section boundaries for tech vs football.
lines = src.split('\n')
football_start = next(i for i, l in enumerate(lines) if 'FOOTBALL' in l and 'Questions' in l)

TECH_TOPICS = [
    ('Large Language Models', [
        'large language model', ' llm', 'llm)', 'transformer', 'prompt engineering',
        'context window', 'retrieval-augmented', 'rag)', ' rag ', 'fine-tun', 'chain-of-thought',
        'multimodal', 'ai agent', 'foundation model', 'knowledge distillation', 'rlhf',
        'token', 'constitutional ai', 'gpt', 'in-context learning',
    ]),
    ('Robotics', [
        'robot', 'slam', 'cobot', 'exoskeleton', 'end effector', 'grasp', 'swarm robot',
        'uncanny valley', 'teleoperat', 'path planning', 'inverse kinematics', 'digital twin',
        'soft robotics', ' agv', ' amr', 'moravec', 'actuator', 'manipulat',
    ]),
    ('Cybersecurity & Networks', [
        'security', 'encrypt', 'password', 'phishing', 'malware', 'ransomware', 'firewall',
        'zero-trust', 'zero trust', 'zero-day', 'zero day', ' vpn', 'two-factor', '2fa',
        'authenticat', 'vulnerab', 'penetration test', 'cia triad', 'social engineering',
        'sql injection', 'ddos', 'denial-of-service', 'breach', 'cyber', 'e2ee',
        'end-to-end encryption', 'hacker', 'exploit', 'attack surface',
    ]),
    ('Programming & Web Systems', [
        'docker', 'kubernetes', 'ci/cd', 'continuous integration', 'api ', 'http', 'html',
        'css', 'javascript', 'database', 'cloud comput', 'devops', 'git ', 'osi model',
        'tls', 'ssl', 'load balanc', 'container', 'source code', 'software develop',
        'oop', 'framework', 'web application', 'web server', 'web develop', 'algorithm',
        'programming language', 'debug', 'compiler', 'open source software',
    ]),
    ('Data Science & Analytics', [
        'data set', 'dataset', 'statistic', 'regression', 'cluster', 'feature engineering',
        'a/b test', 'random forest', 'gradient boosting', 'time series', 'dimensionality',
        'data governance', 'k-means', 'analytics', 'correlation', 'bias-variance',
        'exploratory data', 'xgboost', 'data scien', 'descriptive', 'predictive analytics',
        'prescriptive',
    ]),
    ('Ethics, Society & Future Tech', [
        'social justice', 'inequality', 'surveillance capitalism', 'responsible ai',
        'ai for good', 'technology transfer', 'automation paradox', 'carbon footprint',
        'algorithmic accountability', 'regulation', 'future of work', 'data sovereignty',
        'digital divide', 'digital inequality', 'misinformation', 'ai governance',
        'bias in ai', 'ai bias', 'ai regulation', 'critical', "nigeria's development",
        'fintech', 'edge ai', 'internet of things', ' iot ', 'healthcare in africa',
        'precision agriculture', '5g', 'digital payments',
    ]),
    ('AI Foundations', []),  # fallback bucket
]

FOOTBALL_TOPICS = [
    ('Laws & Officiating', [
        'red card', 'yellow card', 'free kick', 'var ', 'video assistant', 'encroachment',
        'advantage rule', 'fourth official', 'half-time', 'abandon', 'offside', 'penalty kick',
        'referee', 'foul', 'handball', 'law of the game', 'added time', 'stoppage time',
        'throw-in', 'corner kick', 'goal kick', 'misconduct', 'sending off', 'laws of football',
        'yard box', 'substitut', 'goalkeeper', 'shootout', 'penalty spot', 'players on the pitch',
        'squad size', 'kick-off', 'extra time', 'away goals', 'offside trap', 'goal line',
        'pitch dimensions', 'match officials', 'linesman', 'assistant referee', 'suspension',
        'booking', 'caution', 'match ball', 'kit colours', 'away kit', "captain's armband",
    ]),
    ('Tactics & Playing Styles', [
        'counter-attack', 'defensive line', 'box-to-box', 'number 10', 'formation',
        'possession', 'pressing', 'tiki-taka', 'gegenpress', 'wing-back', 'false nine',
        'man-marking', 'zonal marking', 'tactic', 'playing style', 'high line', 'low block',
    ]),
    ('Competitions & History', [
        'world cup', 'fa cup', 'la liga', 'caf champions league', 'ligue 1', 'serie a',
        'premier league', 'bundesliga', 'champions league', "ballon d'or", 'record',
        'consecutive', 'title', 'tournament', 'olympics', 'trophy', 'history of football',
        'founded', 'established',
    ]),
    ('Nigerian & African Football', [
        'nigeria', 'super eagles', 'super falcons', 'aiteo', 'nff', 'african football',
        'afcon', 'africa cup of nations', 'caf ', 'ndidi', 'osimhen', 'okocha', 'kanu',
        'atlanta 1996', 'west africa', 'mikel', 'iheanacho', 'aina', 'chukwueze', 'lookman',
        'oshoala', 'keshi', 'amokachi', 'yekini', 'eguavoen', 'usa 1994', 'flying eagles',
        'golden eaglets', 'egypt', 'ghana', 'senegal', 'ivory coast', 'cameroon', 'morocco',
        'zamalek', 'al ahly', 'african nations', "south africa's football",
    ]),
    ('World Cup & International', [
        '2026', 'usa/canada/mexico', 'international football', 'fifa ranking', 'qualif',
        'host nation', 'expanded format', '48 team', 'international break',
    ]),
    ('Club & Culture', []),  # fallback
]


def classify(text, topics):
    text_l = text.lower()
    best_topic, best_score = topics[-1][0], 0
    for topic, kws in topics:
        score = sum(1 for kw in kws if kw in text_l)
        if score > best_score:
            best_score = score
            best_topic = topic
    return best_topic


out_lines = []
tagged = 0
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('{q:'):
        topics = FOOTBALL_TOPICS if i >= football_start else TECH_TOPICS
        topic = classify(line, topics)
        # insert topic as first field in the object
        new_line = line.replace('{q:', "{topic:'%s',q:" % topic, 1)
        out_lines.append(new_line)
        tagged += 1
    else:
        out_lines.append(line)

assert tagged == 544, f"expected 544 questions tagged, got {tagged}"

with open(PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print(f"Tagged {tagged} questions.")

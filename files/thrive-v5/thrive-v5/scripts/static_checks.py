#!/usr/bin/env python3
"""Static QA checks for the THRIVE website v5."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles = 0; self.descriptions = 0; self.canonicals = 0
        self.links = []; self.images = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'title': self.titles += 1
        if tag == 'meta' and d.get('name','').lower() == 'description': self.descriptions += 1
        if tag == 'link' and d.get('rel','').lower() == 'canonical': self.canonicals += 1
        if tag == 'a' and 'href' in d: self.links.append(d['href'])
        if tag == 'img': self.images.append(d)

def main():
    errors = []
    for page in sorted(ROOT.glob('*.html')):
        parser = PageParser()
        parser.feed(page.read_text(encoding='utf-8', errors='ignore'))
        rel = page.relative_to(ROOT)
        if parser.titles != 1:
            errors.append(f'{rel}: expected 1 <title>, found {parser.titles}')
        if parser.descriptions != 1:
            errors.append(f'{rel}: expected 1 meta description, found {parser.descriptions}')
        if parser.canonicals != 1:
            errors.append(f'{rel}: expected 1 canonical link, found {parser.canonicals}')
        for href in parser.links:
            if href.startswith(('http://','https://','mailto:','tel:','#','javascript:')): continue
            target = href.split('#', 1)[0]
            if target and not (ROOT / target).exists():
                errors.append(f'{rel}: broken internal href → {href}')
        for img in parser.images:
            if 'alt' not in img:
                errors.append(f'{rel}: <img> missing alt → {img.get("src","unknown")}')

    required = ['robots.txt','sitemap.xml','privacy.html','terms.html','_headers','.well-known/security.txt']
    for req in required:
        if not (ROOT / req).exists():
            errors.append(f'Missing required file: {req}')

    if errors:
        print('❌ Static checks FAILED:')
        for e in errors: print(f'  • {e}')
        sys.exit(1)
    else:
        print(f'✅ Static checks passed — {len(list(ROOT.glob("*.html")))} pages checked.')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Static QA checks for the Trivefoundation website."""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles = 0
        self.descriptions = 0
        self.canonicals = 0
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "title":
            self.titles += 1
        if tag == "meta" and data.get("name", "").lower() == "description":
            self.descriptions += 1
        if tag == "link" and data.get("rel", "").lower() == "canonical":
            self.canonicals += 1
        if tag == "a" and "href" in data:
            self.links.append(data["href"])
        if tag == "img":
            self.images.append(data)

def main():
    errors = []
    for page in sorted(ROOT.glob("*.html")):
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8", errors="ignore"))
        rel = page.relative_to(ROOT)
        if parser.titles != 1:
            errors.append(f"{rel}: expected exactly 1 title tag, found {parser.titles}")
        if parser.descriptions != 1:
            errors.append(f"{rel}: expected exactly 1 meta description, found {parser.descriptions}")
        if parser.canonicals != 1:
            errors.append(f"{rel}: expected exactly 1 canonical link, found {parser.canonicals}")
        for href in parser.links:
            if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
                continue
            target = href.split("#", 1)[0]
            if target and not (ROOT / target).exists():
                errors.append(f"{rel}: broken internal href {href}")
        for image in parser.images:
            if "alt" not in image:
                errors.append(f"{rel}: image missing alt attribute: {image.get('src', 'unknown')}")
    for required in ("robots.txt", "sitemap.xml", "privacy.html", "terms.html", "_headers", ".well-known/security.txt"):
        if not (ROOT / required).exists():
            errors.append(f"missing required standards file: {required}")
    # Brand guardrails (see BRAND.md)
    for required in ("assets/logo.svg", "assets/logo-white.svg", "assets/favicon.svg",
                     "assets/fonts/fredoka-latin-wght.woff2", "assets/fonts/lexend-latin-wght.woff2"):
        if not (ROOT / required).exists():
            errors.append(f"missing brand asset: {required}")
    for path in sorted(ROOT.glob("*.html")) + [ROOT / "js/config.js", ROOT / "js/components.js", ROOT / "css/style.css"]:
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for wrong in ("THRIVE Foundation", "TriveFoundation", "Trive " + "Foundation"):
            if wrong in text:
                errors.append(f"{rel}: write the organisation as 'Trivefoundation', one word (found '{wrong}')")
        if "fonts.googleapis.com" in text or "fonts.gstatic.com" in text:
            errors.append(f"{rel}: fonts are self-hosted; remove the Google Fonts reference (CSP blocks it)")
    if errors:
        print("Static checks failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Static checks passed.")

if __name__ == "__main__":
    main()

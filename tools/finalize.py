#!/usr/bin/env python3
"""
finalize.py — make the course markdown safe for the MkDocs site.

Idempotent: run it repeatedly without harm. It fixes the things that would
break the published site (https://ijk37.com/python-fundamentals/):

  1. Ensures the branded header (banner + live-site badge + section badge +
     two-way nav) exists on every PROJECT README (04-projects/*/README.md);
     inserts it right after the first H1 if a README is missing it. Section
     READMEs (01-notes, 02-exercises, 04-projects overview, 05-resources) are
     maintained by hand and already carry the header, so they are left alone.
  2. Converts raw-HTML nav (<a href="x.md"><img></a>, <a href="x.md">text</a>,
     banner <img>) into MARKDOWN links/images so MkDocs rewrites them to .html
     (raw HTML links are NOT rewritten -> they 404 on the site).
  3. Adds the `markdown` attribute to centered nav divs so links inside them
     get processed.
  4. Retargets root-home links to index.md (depth-aware), since README.md is
     excluded from the build:
        section pages     :  ../README.md    -> ../index.md
        project sub-pages :  ../../README.md -> ../../index.md
                             (keep ../README.md = projects overview)
  5. Points quiz-README links at the quiz app (03-quiz/README.md -> 03-quiz/).

Usage:
    python tools/finalize.py
    python -m mkdocs build     # or: python -m mkdocs serve
"""
import os
import re
import glob

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

SITE = "https://ijk37.com/python-fundamentals/"

LIVE_SITE_BADGE = (
    "[![View the live site — ijk37.com]"
    "(https://img.shields.io/badge/%F0%9F%90%8D_View_the_Live_Site-IJK37.COM-306998"
    "?style=for-the-badge&labelColor=FFD43B)]"
    "(" + SITE + ")"
)

BANNER_LINKED = re.compile(r'<a href="[^"]*"><img src="([^"]*banner\.svg)" alt="([^"]*)"[^>]*></a>')
BANNER_PLAIN = re.compile(r'<img src="([^"]*banner\.svg)" alt="([^"]*)"[^>]*>')
BADGE_LINK = re.compile(r'<a href="([^"]+)"><img src="([^"]+)" alt="([^"]*)"></a>')
TEXT_LINK = re.compile(r'<a href="([^"]+)">([^<]+)</a>')
PROJECT_DIR = re.compile(r'04-projects/04-(\d+)-[^/]+/README\.md$')


def convert_nav(s: str) -> str:
    s = BANNER_LINKED.sub(r'![\2](\1)', s)
    s = BANNER_PLAIN.sub(r'![\2](\1)', s)
    s = BADGE_LINK.sub(r'[![\3](\2)](\1)', s)
    s = TEXT_LINK.sub(r'[\2](\1)', s)
    s = s.replace('<div align="center">', '<div align="center" markdown>')
    return s


def project_header(num: str) -> str:
    """Branded two-way nav header for a project sub-page (depth 2)."""
    section_badge = (
        f'<img src="https://img.shields.io/badge/Project_{num}-Python-306998'
        f'?style=for-the-badge&labelColor=1E4B73" alt="Project {num}">'
    )
    nav = (
        f'[Home](../../index.md) &nbsp;|&nbsp; '
        f'[All Projects](../README.md) &nbsp;|&nbsp; '
        f'[Notes](../../01-notes/README.md) &nbsp;|&nbsp; '
        f'[Exercises](../../02-exercises/README.md) &nbsp;|&nbsp; '
        f'[Quiz Hub](../../03-quiz/)'
    )
    return (
        '<div align="center" markdown>\n\n'
        '![Python: Fundamentals](../../assets/banner.svg)\n\n'
        f'{LIVE_SITE_BADGE}\n\n'
        f'{section_badge}\n\n'
        f'{nav}\n\n'
        '</div>'
    )


def ensure_project_header(path: str, s: str) -> str:
    """Insert the branded header after the first H1 if it is missing."""
    if 'banner.svg' in s:
        return s
    m = PROJECT_DIR.search(path.replace("\\", "/"))
    if not m:
        return s
    block = project_header(m.group(1))
    lines = s.split('\n')
    out, inserted = [], False
    for ln in lines:
        out.append(ln)
        if not inserted and ln.startswith('# '):
            out.append('')
            out.append(block)
            inserted = True
    if not inserted:
        return block + '\n\n' + s
    return '\n'.join(out)


def fix_file(path: str) -> bool:
    s = open(path, encoding="utf-8").read()
    orig = s
    norm = path.replace("\\", "/")
    depth = norm.count("/")

    s = ensure_project_header(path, s)
    s = convert_nav(s)

    # quiz README -> quiz hub
    s = s.replace("](../../03-quiz/README.md)", "](../../03-quiz/)")
    s = s.replace("](../03-quiz/README.md)", "](../03-quiz/)")
    s = s.replace("](03-quiz/README.md)", "](03-quiz/)")

    # root-home retarget (depth aware)
    if depth >= 2:
        s = s.replace("](../../README.md)", "](../../index.md)")
    else:
        s = s.replace("](../README.md)", "](../index.md)")

    if s != orig:
        open(path, "w", encoding="utf-8", newline="\n").write(s)
        return True
    return False


def main():
    files = (
        glob.glob("01-notes/*.md")
        + glob.glob("02-exercises/*.md")
        + ["01-notes/README.md", "02-exercises/README.md",
           "04-projects/README.md", "05-resources/README.md"]
        + glob.glob("04-projects/*/README.md")
    )
    changed = sum(fix_file(f) for f in sorted(set(files)) if os.path.exists(f))
    print(f"finalize: fixed {changed} file(s). Now run:  python -m mkdocs build")


if __name__ == "__main__":
    main()

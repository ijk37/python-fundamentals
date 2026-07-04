# Site Design Blueprint

How this repository is structured so that **one set of Markdown files works two ways at once**:

1. **Browsable on GitHub** — every folder has a branded `README.md`, links resolve, badges render.
2. **Published as a polished site** — the same files build into a [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) site, auto-deployed to GitHub Pages at a custom domain.

Follow this document to reproduce the "repo **and** live site from the same files" setup. It mirrors the layout used by the companion `network-systems` repo, using the **Python blue (#306998) + yellow (#FFD43B)** palette — the lighter of the two sibling course sites (see `data-analytics-python` for the deeper variant).

> [!NOTE]
> This file lives in `assets/` and is excluded from the built site (it is internal documentation, not a course page).

---

## 1. The core idea

A normal MkDocs project keeps docs in a `docs/` subfolder. That makes GitHub browsing ugly (everything nested under `docs/`). Instead, this repo builds **from the repository root** (`docs_dir: .`) so:

- The folders you see on GitHub (`01-notes/`, `02-exercises/`, …) **are** the site's content.
- Each folder's `README.md` is both the GitHub folder landing page **and** the site section index.

Two settings make links behave identically in both places:

| Setting | Value | Why |
| --- | --- | --- |
| `docs_dir` | `.` | Build from repo root, not `docs/` |
| `use_directory_urls` | `false` | URLs mirror file paths, so relative `.md` links map 1:1 to `.html` |

---

## 2. Repository structure

```
python-fundamentals/
├── .github/workflows/deploy.yml   # CI: build + deploy to GitHub Pages
├── 01-notes/            # Topic notes (one .md per concept) + README index
├── 02-exercises/        # Practice sets mirroring the notes + README index
├── 03-quiz/             # Static quiz app (own index.html, owns this URL path)
├── 04-projects/         # 32 project folders, each with main.py + README.md
├── 05-resources/        # Only README.md is published; slides stay local
│   ├── .gitignore       # Ignores *.pptx, *.txt (local-only material)
│   └── README.md
├── assets/
│   ├── banner.svg       # Hero banner embedded on every section README
│   ├── images/          # favicon.svg, python-logo.svg
│   ├── stylesheets/extra.css   # Brand theme (blue + yellow)
│   ├── javascripts/extra.js
│   └── site_design.md   # ← this file (excluded from build)
├── overrides/           # MkDocs theme custom_dir (theme tweaks)
├── tools/finalize.py    # Idempotent pre-build fixer (see §8)
├── index.md             # Site home page (REQUIRED at root, docs_dir=.)
├── README.md            # GitHub landing page (excluded from build)
├── 01-notes.md … 04-projects.md   # Root "shortcut" pages → deep-link to live site
├── mkdocs.yml           # Site config (REQUIRED at root)
├── requirements.txt     # Python packages used by the course projects
└── requirements-docs.txt  # Build deps for the site (used by CI)
```

**Load-bearing files that cannot be hidden or moved:** `.github/`, `mkdocs.yml`, `index.md`, `requirements-docs.txt`, `assets/`, `overrides/`, `tools/`, and the content folders. Hiding any of them via `.gitignore` breaks the deploy.

> Note: the course's `requirements.txt` lists the runtime packages learners install (NumPy, Pandas, Matplotlib …). The **site build** uses a separate `requirements-docs.txt` (mkdocs-material + plugins) so the two concerns never collide.

---

## 3. MkDocs configuration (`mkdocs.yml` essentials)

```yaml
site_name: Python — Fundamentals
site_url: https://ijk37.com/python-fundamentals/
repo_url: https://github.com/ijk37/python-fundamentals

docs_dir: .                       # build from repo root
site_dir: ../python-fundamentals-site   # build OUTSIDE the repo
use_directory_urls: false         # links map 1:1 to file paths

exclude_docs: |                   # keep these OUT of the built site
  mkdocs.yml
  requirements.txt
  requirements-docs.txt
  .gitignore
  tools/**
  assets/site_design.md
  05-resources/**                 # exclude the folder …
  !05-resources/README.md         # … but re-include just its README (negation)
  01-notes.md                     # root shortcut pages are GitHub-only
  02-exercises.md
  03-quiz.md
  04-projects.md

theme:
  name: material
  custom_dir: overrides
  logo: assets/images/python-logo.svg
  favicon: assets/images/favicon.svg
  palette:                        # light + dark, both using custom brand colors
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: custom
      accent: custom
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: custom
      accent: custom
  features:
    - navigation.indexes          # a folder's README.md becomes that section's index
    - navigation.instant
    - navigation.top
    - toc.follow

plugins:
  - same-dir                      # REQUIRED when docs_dir: .
  - search
  - callouts                      # renders GitHub-style > [!NOTE] as admonitions

markdown_extensions:
  - admonition
  - attr_list                     # enables { .class } on links → the home-page cards
  - md_in_html                    # lets Markdown links inside <div markdown> get rewritten
  - pymdownx.superfences
  - toc: { permalink: true }
```

Key plugin/extension roles:
- **`same-dir`** — required for `docs_dir: .`, otherwise the build errors.
- **`callouts`** — so `> [!NOTE]`, `> [!TIP]` (quotes on GitHub) become styled admonitions on the site. One syntax, both platforms.
- **`md_in_html` + `<div markdown>`** — MkDocs rewrites Markdown links to `.html`, but **not** raw `<a href="x.md">`. So all navigation must be **Markdown links inside a `markdown`-enabled div**, never raw HTML anchors (see §8).
- **`attr_list`** — lets `[Text](url){ .py-card }` become styled cards on the home page.
- **`navigation.indexes`** — turns each `README.md` into its folder's index, so section URLs are clean directories.

---

## 4. Branding & theme

**Palette** (defined once as CSS variables in `assets/stylesheets/extra.css`, wired into Material's own variables):

```css
:root {
  --py-blue:        #306998;
  --py-blue-dark:   #1e4b73;
  --py-blue-bright: #4b8bc4;
  --py-yellow:      #ffd43b;
  --py-yellow-deep: #e6b800;

  --md-primary-fg-color: #306998;   /* Material header/links */
  --md-accent-fg-color:  #e6b800;
}
[data-md-color-scheme="slate"] { /* dark-mode overrides — brighter yellow */ }
```

Reusable brand elements:
- **Hero banner** — `assets/banner.svg` (blue gradient + yellow accent + a `>_` code motif), embedded as a Markdown image at the top of every section README.
- **Home-page cards** — `attr_list` links with `.py-card .py-card-<name>` classes; each card gets a colored left border. Add a card by adding one line in `index.md` and one `.py-card-<name>` rule in `extra.css`.
- **Badges** — [shields.io](https://shields.io) `for-the-badge` style. The prominent **"View the Live Site"** badge uses the blue/yellow theme (yellow `#FFD43B` label + blue `#306998` message) with a 🐍 mark, so it stands out while staying on-brand. It sits under the banner on every README.
- **Yellow H2 underlines, blue table headers** — small `extra.css` touches that make plain Markdown pages look designed.

---

## 5. Home page (`index.md`)

- Front matter `hide: [navigation]` for a clean landing (no left tree on the home page).
- A `.py-hero-grid` of cards (Notes, Exercises, Quiz Hub, Projects, Resources) — the primary in-body navigation, so it works even when the sidebar is hidden.
- Because `README.md` and `index.md` would collide, **`README.md` is excluded from the build** and `index.md` is the site home. Keep the two in rough sync by hand.

---

## 6. Two-way navigation pattern

Every section `README.md` starts with the same block:

```markdown
# 📘 Section Title

<div align="center" markdown>

![Python: Fundamentals](../assets/banner.svg)

[![View the live site — ijk37.com](…theme badge…)](https://ijk37.com/python-fundamentals/)

<img src="…section badge…" alt="Section">

[Home](../index.md) | [Notes](../01-notes/README.md) | [Exercises](../02-exercises/README.md) | [Quiz Hub](../03-quiz/) | [Projects](../04-projects/README.md)

</div>
```

Rules that keep it working in **both** GitHub and the site:
- `<div align="center" markdown>` — the `markdown` attribute is what lets MkDocs process (and rewrite) the links inside.
- **Banner and nav are Markdown**, not raw HTML `<a>`/`<img>` — raw HTML links are **not** rewritten and would 404 on the site.
- Links use relative paths; with `use_directory_urls: false` they map straight to the built `.html`.

---

## 7. Special folders

**`03-quiz/` (static app owns its URL).** It has its own `index.html`, so the site nav points at `03-quiz/index.html` and other pages link to `../03-quiz/`. Its `README.md` is excluded from the build (it would conflict with `index.html`). See §10 for the engine.

**`05-resources/` (publish one page, hide the rest).** The folder holds local-only lecture slides. An inner `05-resources/.gitignore` keeps `*.pptx *.txt` out of git. The build publishes **only** `README.md` via the `exclude_docs` negation.

**Root shortcut pages (`01-notes.md` … `04-projects.md`).** GitHub-only mini landing pages (excluded from the build) that show the "View the Live Site" badge plus a button deep-linking to that section on the live site.

---

## 8. `tools/finalize.py` — the idempotent fixer

Runs **before each build** (locally and in CI) and self-corrects. Idempotent — safe to run repeatedly. It:

1. **Ensures the branded header** (banner + live-site badge + section badge + nav) exists on every section/project README; inserts it after the H1 if a README is missing it.
2. Converts raw-HTML nav (`<a href="x.md"><img></a>`, banner `<img>`) into **Markdown** links/images.
3. Adds the `markdown` attribute to centered `<div align="center">` nav blocks.
4. Retargets root-home links to `index.md` (depth-aware), since `README.md` is excluded.
5. Points quiz-README links at the quiz app (`03-quiz/README.md` → `03-quiz/`).
6. Fixes note image refs to `../assets/images/…` where applicable.

Run it with `python tools/finalize.py`, then `python -m mkdocs build`.

---

## 9. Deployment (GitHub Actions → Pages → custom domain)

**Workflow** `.github/workflows/deploy.yml`: on push to `main`, it checks out, `pip install -r requirements-docs.txt`, runs `python tools/finalize.py`, `mkdocs build --site-dir _site`, then `upload-pages-artifact` + `deploy-pages`. Needs `permissions: { pages: write, id-token: write }`.

**One-time setup:**
1. GitHub → **Settings → Pages → Build and deployment → Source = "GitHub Actions"** (⚠️ *not* "Deploy from a branch").
2. Add `_site/` and `/site/` to `.gitignore` (never commit the build output).

**Custom domain.** The domain `ijk37.com` is set on the **user site** repo (`<user>.github.io`), and GitHub Pages **cascades the user domain to every project site** on the account, so this project is served at `https://ijk37.com/python-fundamentals/` — **no `CNAME` file needed here**. Set `site_url` to the real URL so sitemaps/canonical links use it, and set the repo's **About → Website** field to that URL.

---

## 10. Reusable quiz engine (`03-quiz/`)

A self-contained, dependency-free quiz engine (plain HTML + CSS + JS) that runs from static files. A topic **hub** (`index.html`, card grid) + a **quiz engine** (`quiz.html`, run via `?topic=<id>`). Each attempt draws a **random subset** from a larger **pool**; answer options are **reshuffled every render** (kills position bias); a sidebar gives a question navigator, elapsed timer, and Finish button; results show score/%/grade/time plus a full per-question review.

**File structure:**
```
03-quiz/
├── index.html                 # hub → links to quiz.html?topic=<id>
├── quiz.html                  # engine: all logic + inline styling
├── data.js                    # TOPICS, QUIZ_CONFIG, QUESTIONS = {}, chapter 01
├── data-02.js … data-11.js    # one file per chapter (Python topics 02–11)
├── data-mixed-1.js … -5.js    # cumulative mixed quizzes built from the pools
└── README.md
```

**Data format:**
```js
const TOPICS = [ { id: "01", title: "Setup & Environment" }, { id: "mixed-1", title: "Final Mixed 1" } ];
const QUIZ_CONFIG = { defaultAttempt: 20, attempt: { "mixed-3": 50, "mixed-5": 60 } };
const QUESTIONS = {};
QUESTIONS["01"] = [
  { q: "Question?", options: ["A","B","C","D"], answer: 1, explain: "Why B is correct." },
];
```

**Script load order** (in both `index.html` and `quiz.html`): `data.js` → base `data-NN.js` → `data-mixed-*.js` **last** (so mixed quizzes sample the enlarged pools) → the inline engine `<script>`.

**Theme:** dark, inline in each HTML `<style>` — blue/yellow accents matching the site brand.

**Validation without Node:** every question needs `q/options/answer/explain`, and `0 ≤ answer < options.length`.

---

## 11. Replicate this in a new repo — checklist

1. **Content first.** Put `README.md` in each top-level content folder; write `index.md` as the home page.
2. **Add MkDocs config.** `mkdocs.yml` with `docs_dir: .`, `use_directory_urls: false`, `same-dir` + `callouts` plugins, `md_in_html` + `attr_list`, custom palette. `requirements-docs.txt` with `mkdocs-material`, `mkdocs-callouts`, `mkdocs-same-dir`.
3. **Brand it.** Copy `assets/` (banner, `extra.css` variables, favicon/logo); adjust colors and the live-site badge URL.
4. **Standardize navigation.** Every README uses the `<div align="center" markdown>` block with Markdown (not raw-HTML) links + the banner + the live-site badge.
5. **Add `tools/finalize.py`** and run it before building.
6. **Add the CI workflow** and set **Pages Source = GitHub Actions**.
7. **Wire the domain** (user-site cascade) and set `site_url` + the repo's About → Website field.
8. **Verify:** `python tools/finalize.py && python -m mkdocs build` with **zero warnings**, then check the deployed nav, links, and the quiz app.

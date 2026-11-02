# Asad Mujeeb — Portfolio

A fast, accessible, dark-and-gold portfolio built with **Flask** and rendered to plain static HTML for **Netlify**.
Content lives in one file (`data.py`), so updating the site never means touching a template.

## Features
- Dark and light themes (saved per visitor), responsive down to small phones
- Works without JavaScript; JS only adds the theme toggle, mobile menu, and project filter
- Contact form handled by **Netlify Forms** — no backend or API key needed
- SEO basics: per-page titles and descriptions, canonical URLs, Open Graph / Twitter cards, JSON-LD profile, `sitemap.xml`, `robots.txt`, custom 404
- Self-hosted fonts and optimized WebP images — no third-party requests for assets
- Accessibility: skip link, visible focus, WCAG AA contrast in both themes, reduced-motion support

## Project structure
```
├── app.py                 # Flask routes + SEO context
├── data.py                # ALL site content — edit this to update the site
├── build.py               # Renders every route to dist/ (what Netlify publishes)
├── netlify.toml           # Build command, security + cache headers
├── Procfile               # Optional: run the Flask app on Render/Railway
├── requirements.txt
├── templates/             # base, pages, and shared partials (_job_header, _project_card)
└── static/
    ├── css/main.css
    ├── js/main.js
    ├── fonts/             # Playfair Display + DM Sans (woff2)
    ├── images/            # profile, logos, awards, volunteer photos, og-image.png
    ├── favicon.svg
    └── Asad_Mujeeb_Resume.pdf
```

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py            # http://127.0.0.1:5000  (live Flask server)
python build.py          # writes the static site to dist/
```
Locally, the contact form posts to the thank-you page but the message is **not** sent anywhere — delivery only works once deployed on Netlify.

## Deploy on Netlify
1. Connect the repo. `netlify.toml` already sets the build command (`python build.py`) and publish folder (`dist`).
2. **Contact form:** after the first deploy, open *Site configuration → Forms* and add an email notification so messages reach your inbox. The form is detected automatically.
3. **Canonical URLs and sitemap:** Netlify's `$URL` is used automatically. If you use a custom domain, set `SITE_URL=https://your-domain.com` under *Environment variables*.

## Updating content
Everything is in `data.py`:

| To change | Edit |
|-----------|------|
| Name, title, contact links, hero stats | `PERSONAL` |
| About text (`**bold**` and `[link](url)` supported) | `ABOUT` |
| Skills | `SKILL_GROUPS`, `BUSINESS_SKILLS` |
| Projects | `PROJECTS` — add `'github': '...'` and/or `'demo': '...'` and labelled links appear on the card |
| Jobs | `EXPERIENCE` |
| Certificates | `CERTIFICATIONS` — `credential_id` is shown only if set |
| Awards, community roles, education | `AWARDS`, `VOLUNTEER`, `EDUCATION` |

New images: save as WebP (max ~1400px wide) in `static/images/` and reference the path in `data.py`.

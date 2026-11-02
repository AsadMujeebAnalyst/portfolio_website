"""
Portfolio site — Flask app that is also rendered to static HTML by build.py
for Netlify. Content lives in data.py; this file only wires routes.
"""
import hashlib
import os
import re
from datetime import datetime
from functools import lru_cache

from flask import Flask, render_template, request, url_for
from markupsafe import Markup, escape

import data

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:  # python-dotenv is optional
    pass

app = Flask(__name__)

# Absolute site URL (no trailing slash). Netlify exposes the primary URL as
# $URL at build time; set SITE_URL to override (e.g. for a custom domain).
SITE_URL = (os.environ.get('SITE_URL') or os.environ.get('URL') or '').rstrip('/')

PAGE_META = {
    'index': ('Asad Mujeeb — Data Analyst & BI Specialist',
              'Data Analyst in Multan, Pakistan specializing in Business Intelligence, Power BI, '
              'Python and product analytics. Dashboards, automation and ML that drive decisions.'),
    'about': ('About — Asad Mujeeb',
              'Data Analyst & BI Specialist from Multan, Pakistan. Background, education and the '
              'way I turn messy data into decisions.'),
    'experience': ('Experience — Asad Mujeeb',
                   'Work history across mobile app analytics, machine learning and business '
                   'intelligence: Dream Edge Technologies, Blue Cascade and Ai NEURALZ.'),
    'projects': ('Projects & Case Studies — Asad Mujeeb',
                 'Selected data projects across BI dashboards, machine learning, automation and '
                 'analytics engineering, each with a measurable outcome.'),
    'certifications': ('Certifications — Asad Mujeeb',
                       'Verified credentials from Google, freeCodeCamp, DataCamp and Codecademy '
                       'covering Business Intelligence, Machine Learning, Python and SQL.'),
    'volunteer': ('Community & Leadership — Asad Mujeeb',
                  'Data Science Lead at The Youth Matrix and Microsoft Learn Student Ambassador: '
                  'workshops, mentorship and hands-on analytics for students.'),
    'contact': ('Contact — Asad Mujeeb',
                'Get in touch about full-time data analytics roles, freelance projects or '
                'interesting data challenges.'),
    'thank_you': ('Message sent — Asad Mujeeb', 'Thanks for getting in touch.'),
    'not_found': ('Page not found — Asad Mujeeb', 'That page does not exist.'),
}


@lru_cache(maxsize=None)
def _file_hash(filename):
    path = os.path.join(app.static_folder, filename)
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return '0'


def static_v(filename):
    """Static URL with a content hash, so assets can be cached for a year."""
    return url_for('static', filename=filename, v=_file_hash(filename))


def rich(text):
    """Tiny, safe markup for data.py strings: **bold** and [text](url)."""
    out = str(escape(text))
    out = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', out)
    out = re.sub(
        r'\[([^\]]+)\]\((https?://[^)\s]+)\)',
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', out)
    return Markup(out)


app.jinja_env.filters['rich'] = rich


@app.context_processor
def inject_globals():
    endpoint = request.endpoint or 'not_found'  # no endpoint means an unknown URL
    title, description = PAGE_META.get(endpoint, PAGE_META['index'])
    # Pages are built as <name>/index.html, so their canonical URL ends in "/".
    path = request.path if request.path.endswith('/') else request.path + '/'
    return {
        'personal': data.PERSONAL,
        'nav': data.NAV,
        'site_url': SITE_URL,
        'page_title': title,
        'page_description': description,
        'canonical': f'{SITE_URL}{path}' if SITE_URL else '',
        'og_image': f'{SITE_URL}{static_v("images/og-image.png")}' if SITE_URL else '',
        'static_v': static_v,
        'now_year': datetime.now().year,
    }


@app.route('/')
def index():
    return render_template(
        'index.html',
        skill_groups=data.SKILL_GROUPS,
        projects=data.PROJECTS[:3],
        experience=data.EXPERIENCE,
        certifications=data.CERTIFICATIONS,
        volunteer=data.VOLUNTEER,
        about=data.ABOUT[:2],
    )


@app.route('/about')
def about():
    return render_template(
        'about.html', about=data.ABOUT, education=data.EDUCATION,
        awards=data.AWARDS, skill_groups=data.SKILL_GROUPS,
        business_skills=data.BUSINESS_SKILLS)


@app.route('/experience')
def experience():
    return render_template('experience.html', experience=data.EXPERIENCE)


@app.route('/projects')
def projects():
    categories = sorted({p['category'] for p in data.PROJECTS})
    return render_template('projects.html', projects=data.PROJECTS, categories=categories)


@app.route('/certifications')
def certifications():
    return render_template('certifications.html', certifications=data.CERTIFICATIONS)


@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html', volunteer=data.VOLUNTEER)


@app.route('/contact')
def contact():
    return render_template('contact.html')


# On Netlify the contact form is handled by Netlify Forms (no backend needed)
# and redirects here. POST is accepted so the same form also works locally,
# but locally the message is not stored or sent anywhere.
@app.route('/thank-you', methods=['GET', 'POST'])
def thank_you():
    return render_template('thank_you.html')


@app.route('/404')
def not_found():
    return render_template('404.html')


@app.errorhandler(404)
def handle_404(_error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

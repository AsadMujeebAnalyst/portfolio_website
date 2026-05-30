from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os
import json
import time
try:
    import urllib.request as urlreq
    import urllib.error as urlerr
except ImportError:
    urlreq = None
    urlerr = None

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'asad-portfolio-2026')


# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────

SKILLS = {
   'Technical': [
    # Row 1: Core Skills (Most Important)
    {'name': 'Python',           'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'},
    {'name': 'MySQL',            'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg'},
    {'name': 'Machine Learning', 'logo': 'https://img.icons8.com/color/96/artificial-intelligence.png'},
    {'name': 'Tableau',          'logo': 'https://img.icons8.com/color/96/tableau-software.png'},
    {'name': 'Power BI',         'logo': 'https://img.icons8.com/color/96/power-bi.png'},
    {'name': 'Pandas',           'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg'},
    
    # Row 2: Supporting Tools & Specializations
    {'name': 'Excel',            'logo': 'https://img.icons8.com/color/96/microsoft-excel-2019--v1.png'},
    {'name': 'Firebase',         'logo': 'https://img.icons8.com/color/96/firebase.png'},
    {'name': 'Google Analytics', 'logo': 'https://img.icons8.com/color/96/google-analytics.png'},
    {'name': 'Flask',            'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg'},
    {'name': 'Git',              'logo': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg'},
    {'name': 'n8n',              'logo': 'https://avatars.githubusercontent.com/u/45487711?s=200&v=4'},
],
    'Business': [
        'Translating Data into Actionable Insights',
        'Stakeholder Management & Requirements Gathering',
        'Root-Cause & Diagnostic Analytics',
        'Data-Driven Decision Support',
        'Funnel, Cohort & Retention Analysis',
        'Executive Reporting & Data Storytelling',
        'Cross-Functional Collaboration',
        'Data Literacy Coaching for Teams',
    ],
}

PROJECTS = [
    {
        'id': 1,
        'title': 'Sales Performance Dashboard',
        'subtitle': 'Power BI · DAX · SQL Server',
        'tool': 'Power BI',
        'tool_icon': 'powerbi',
        'description': 'Built an end-to-end Power BI solution analyzing sales across 5 regions. Engineered custom DAX measures for YoY growth, rolling averages, and territory ranking — delivered as a boardroom-ready executive report.',
        'impact': '15% increase in quarterly revenue decisions',
        'technologies': ['Power BI', 'DAX', 'SQL Server', 'Power Query'],
        # 'github': 'https://github.com/yourusername/sales-dashboard',
        # 'demo': 'https://app.powerbi.com/view?r=...',
        'category': 'BI & Dashboards',
        'color': '#F2C94C',
    },
    {
        'id': 2,
        'title': 'Customer Segmentation Engine',
        'subtitle': 'Python · Scikit-learn · Pandas',
        'tool': 'Machine Learning',
        'tool_icon': 'ml',
        'description': 'Applied RFM modeling and K-Means clustering in Python to segment 50K+ customers. Integrated results into a marketing automation workflow that personalizes messaging per cluster.',
        'impact': '25% higher campaign conversion rate',
        'technologies': ['Python', 'Pandas', 'Scikit-learn', 'Matplotlib', 'Seaborn'],
        # 'github': 'https://github.com/yourusername/customer-segmentation',
        # 'demo': None,
        'category': 'Machine Learning',
        'color': '#56CCF2',
    },
    {
        'id': 3,
        'title': 'Healthcare Readmission Analytics',
        'subtitle': 'Tableau · MySQL · Time Series',
        'tool': 'Tableau',
        'tool_icon': 'tableau',
        'description': 'Designed a Tableau workbook with time-series forecasting to identify high-risk patients pre-discharge. Built MySQL stored procedures feeding live data into the viz layer.',
        'impact': '25% reduction in 30-day readmission rates',
        'technologies': ['Tableau', 'MySQL', 'Time Series', 'Statistical Analysis'],
        # 'github': 'https://github.com/yourusername/healthcare-analytics',
        # 'demo': 'https://public.tableau.com/views/...',
        'category': 'BI & Dashboards',
        'color': '#6FCF97',
    },
    {
        'id': 4,
        'title': 'Ai Calling Agent Lead Automation',
        'subtitle': 'n8n · Python · Selenium',
        'tool': 'n8n',
        'tool_icon': 'n8n',
        'description': 'Automated lead generation and outreach for an AI calling agent using n8n workflows. The agent handles Pre-proposals, Post-proposals, and Follow-ups calls from leads generated through google ads',
        'impact': '300+ leads/day automated — 0 manual effort',
        'technologies': ['n8n', 'Python', 'Selenium', 'Webhooks', 'REST APIs'],
        # 'github': 'https://github.com/yourusername/lead-automation',
        # 'demo': None,
        'category': 'Automation',
        'color': '#F97316',
    },
    {
        'id': 5,
        'title': 'WhatsApp Chat Analyzer',
        'subtitle': 'Python · NLP · Streamlit',
        'tool': 'Machine Learning',
        'tool_icon': 'ml',
        'description': 'Final year thesis — a Streamlit web app that parses WhatsApp exports and surfaces behavioral patterns: sentiment trends, activity heatmaps, top contributors, emoji frequency, and message volume forecasting.',
        'impact': 'Thesis project · Top analytical tool for chat data',
        'technologies': ['Python', 'NLP', 'Streamlit', 'Plotly', 'TextBlob'],
        # 'github': 'https://github.com/yourusername/whatsapp-analyzer',
        # 'demo': None,
        'category': 'Machine Learning',
        'color': '#A78BFA',
    },
    {
        'id': 6,
        'title': 'App Monetization KPI Tracker',
        'subtitle': 'GA4 · Firebase · Python',
        'tool': 'Google Analytics',
        'tool_icon': 'ga',
        'description': 'Built a unified KPI framework in Python that pulls ARPU, ARPDAU, LTV, and retention cohorts from Firebase and GA4 APIs, then pushes aggregated metrics to a live Google Sheets dashboard for product teams.',
        'impact': 'Real-time monetization visibility for 10+ apps',
        'technologies': ['Firebase', 'Google Analytics 4', 'Python', 'Google Sheets API'],
        # 'github': 'https://github.com/yourusername/kpi-tracker',
        # 'demo': None,
        'category': 'Analytics Engineering',
        'color': '#FF6B6B',
    },
]

EXPERIENCE = [
    {
        'title': 'Data Analyst (Games & Apps)',
        'company': 'Dream Edge Technologies',
        'logo': 'static\images\det_logo.png',
        'company_website': 'https://topedgetechnologies.com/',
        'linkedin_url': 'https://www.linkedin.com/company/dream-edge-technologies',
        'type': 'Full-time',
        'period': 'Mar 2026 — Present',
        'location': 'Onsite',
        'responsibilities': [
            'Analyzed mobile app & game performance across Firebase Analytics and GA4 for a portfolio of 20+ apps',
            'Built user funnel, retention, and cohort analysis frameworks to optimize onboarding and engagement loops',
            'Monitored monetization KPIs: Ads, IAPs, Subscriptions, ARPU, ARPDAU, and LTV across geo segments',
            'Delivered weekly geo-wise cohort reports surfacing actionable growth opportunities for product teams',
        ],
        'tools': ['Firebase', 'GA4', 'Python', 'Looker Studio', 'Google Sheets'],
    },
    {
        'title': 'Machine Learning Engineer',
        'company': 'Blue Cascade Pakistan',
        'logo': 'static\images\blue_cascade_logo.png',
        'company_website': 'https://bluecascade.org/',
        'linkedin_url': 'https://www.linkedin.com/company/blue-cascade/',
        'type': 'Full-time',
        'period': 'March 2025 — March 2026',
        'location': 'Onsite',
        'responsibilities': [
            'Working on AI Calling Agent using n8n and build end to end data pipelines for the same',
            'Full-stack development using Python, Flask, and MySQL for internal business tools',
            'Led BI initiatives for executive reporting, building Power BI dashboards for C-suite decision-making',
            'Implemented Google Analytics event tracking for e-commerce order and funnel analysis'        ],
        'tools': ['n8n', 'Python', 'PostreSQL', 'Power BI', 'Looker Studio','Database Architecture'],
    },
    {
        'title': 'Business Intelligence Analyst',
        'company': 'Ai NEURALZ',
        'logo': 'static\images\ai_neuralz_logo.jpg',
        'linkedin_url': 'https://www.linkedin.com/company/ai-neuralz/',
        'type': 'Full-time',
        'period': 'May 2024 — October 2024',
        'location': 'Onsite',
        'responsibilities': [
            'Built a real-time Looker dashboard for streaming platform HdHub4u, presented to stakeholders',
            'Developed interactive Power BI dashboards serving sales and marketing teams ',
            'Performed ad-hoc analysis supporting critical product and pricing decisions',
        ],
        'tools': ['Tableau', 'Power BI', 'MySQL', 'Python', 'Looker Studio'],
    },
    {
        'title': 'Data Analytics & Visualization Simulation',
        'company': 'Accenture North America · Forage',
        'logo': None,
        'company_website': 'https://www.theforage.com/simulations',
        'linkedin_url': 'https://www.linkedin.com/company/theforage/',
        'type': 'Job Simulation',
        'period': 'June 2024 — July 2024',
        'location': 'Online',
        'responsibilities': [
            'Advised a hypothetical social media client as a Data Analyst at Accenture',
            'Cleaned, modeled, and analyzed 7 datasets to uncover insights into content trends',
            'Prepared a boardroom PowerPoint deck and video presentation for client and internal stakeholders',
        ],
        'tools': ['Power BI','Excel', 'PowerPoint', 'Data Modeling'],
    },
]

CERTIFICATIONS = [
    {
        'name': 'Business Intelligence',
        'issuer': 'Google',
        'issuer_logo': 'https://img.icons8.com/color/96/google-logo.png',
        'date': 'Aug 13, 2024',
        'credential_id': 'CDJXZEZG0NVD',
        'description': 'Expertise in preparing, modeling, visualizing and analyzing data. Advanced DAX, Power Query, and data model design using Microsoft Power BI.',
        'skills': ['Power BI', 'DAX', 'Power Query', 'Data Modeling'],
        'verify_url': 'https://www.coursera.org/account/accomplishments/professional-cert/CDJXZEZG0NVD',
        'color': '#4285F4',
    },
    {
        'name': 'Machine Learning with Python',
        'issuer': 'freeCodeCamp',
        'issuer_logo': 'https://img.icons8.com/color/96/free-code-camp.png',
        'date': 'July 2023',
        'credential_id': 'fcc-ml-python-v7',
        'description': 'Hands-on experience with supervised & unsupervised learning, neural networks, and data preprocessing pipelines.',
        'skills': ['Data Preprocessing', 'Feature Engineering', 'Model Building', 'Hyperparameter Tuning'],
        'verify_url': 'https://www.freecodecamp.org/certification/AsadMujeeb/machine-learning-with-python-v7',
        'color': '#0A0A23',
    },
    {
        'name': 'Data Analyst Track',
        'issuer': 'DataCamp',
        'issuer_logo': 'data:image/png;base64,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',
        'date': '2022',
        'credential_id': 'dc-analyst-track',
        'description': 'Comprehensive data analysis techniques, predictive modeling, and statistical methods for extracting insights at scale.',
        'skills': ['NumPy', 'Pandas', 'Matplotlib', 'Seaborn'],
        'verify_url': 'https://www.datacamp.com/completed/statement-of-accomplishment/track/89e4b7150c0fca83684be3b236c24b27181505fe',
        'color': '#03EF62',
    },
    {
        'name': 'SQL Track',
        'issuer': 'Codecademy',
        'issuer_logo': 'data:image/png;base64,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',
        'date': 'July 2024',
        'credential_id': 'AWS-CCP-2021-456',
        'description': 'Proficient in SQL for data querying, database design, optimization, and complex multi-table joins and aggregations.',
        'skills': ['Data Query', 'Database Design', 'Data Manipulation', 'Aggregation & Joins'],
        'verify_url': 'https://www.codecademy.com/profiles/Asad-Mujeeb/certificates/042a4e5884e3eb6ea1f2a12be6abb851',
        'color': '#1F4056',
    },
]

# /about “Shields & trophies” — add rows with image, alt, optional caption & href
ABOUT_BADGES = [
    {'image': 'images/img_1.png', 'alt': 'Achievement shield or trophy', 'caption': '', 'href': None},
    {'image': 'images/img_2.png', 'alt': 'Achievement shield or trophy', 'caption': '', 'href': None},
]

VOLUNTEER = [
    {
        'org': 'The Youth Matrix',
        'slug': 'youth-matrix',
        'role': 'Data Science Lead',
        'period': 'May 2025 — Present',
        'description': 'Delivered an online Data Analytics Fellowship empowering students through Power BI, Tableau, SQL, and Excel.',
        'achievements': [
            'Designed hands-on projects allowing participants to apply skills in real-world analysis scenarios',
            'Actively addressed student queries with personalized support on complex concepts',
            'Built a performance tracking system evaluating progress and offering constructive feedback',
        ],
        'logo': 'images/the_youth_matrix_logo.jpeg',
        'announcement': 'images/the_youth_matrix_announcement.jpg',
        'group_photo': 'images/the_youth_matrix_group_photo.jpeg',
    },
    {
        'org': 'Microsoft Learn Student Ambassadors',
        'slug': 'mlsa',
        'role': 'Data Analytics Lead',
        'period': 'August 2024 — April 2025',
        'description': 'Represented Microsoft’s student program locally — hosting workshops, supporting peers with data analytics tooling, and helping onboard new ambassadors to the community.',
        'achievements': [
            'Led sessions and study jams on Power BI, Excel, and storytelling with data for student audiences',
            'Mentored participants through hands-on analytics challenges and presentation best practices',
            'Contributed to community events that connect learners with cloud and modern workplace skills',
        ],
        'logo': 'images/mlsa_logo.webp',
        'announcement': 'images/mlsa_announcement.jpeg',
        'group_photo': 'images/mlsa_group_photo.jpeg',
    },
]

EDUCATION = [
    {
        'degree': 'Bachelor of Information & Communication Technology',
        'institution': 'Bahauddin Zakariya University (BZU)',
        'location': 'Multan, Pakistan',
        'period': '2021 — 2025',
        'gpa': '3.56 / 4.0',
        'thesis': 'WhatsApp Chat Analyzer',
    }
]

PERSONAL = {
    'name': 'Asad Mujeeb',
    'title': 'Data Analyst & BI Specialist',
    'tagline': 'Turning Raw Data Into Strategic Decisions',
    'email': 'asadmujeeb559@gmail.com',
    'phone': '+92 316 6328876',
    'linkedin': 'https://linkedin.com/in/asadmujeeb',
    'github': 'https://github.com/asadmujeeb',
    'resume': '/static/Asad_Mujeeb_Resume.pdf',
    'location': 'Multan | Punjab | Pakistan',
    'stats': [
        {'number': '2+',  'label': 'Years Experience'},
        {'number': '10+',  'label': 'Certifications'},
        {'number': '80%', 'label': 'Reporting Automated'},
        {'number': '1M+', 'label': 'Data Processed'},
    ]
}

# ─────────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────────

@app.route('/')
def index():
    featured = PROJECTS[:3]
    return render_template('index.html',
        personal=PERSONAL,
        skills=SKILLS,
        projects=featured,
        experience=EXPERIENCE,
        education=EDUCATION,
        about_badges=ABOUT_BADGES,
        certifications=CERTIFICATIONS,
        volunteer=VOLUNTEER)

@app.route('/about')
def about():
    return render_template('about.html',
        personal=PERSONAL, education=EDUCATION, about_badges=ABOUT_BADGES)

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html',
        personal=PERSONAL, volunteer=VOLUNTEER)

@app.route('/projects')
def projects():
    category = request.args.get('category', 'All')
    categories = ['All'] + sorted(set(p['category'] for p in PROJECTS))
    filtered = PROJECTS if category == 'All' else [p for p in PROJECTS if p['category'] == category]
    return render_template('projects.html',
        personal=PERSONAL, projects=filtered,
        categories=categories, active_category=category)

@app.route('/experience')
def experience():
    return render_template('experience.html',
        personal=PERSONAL, experience=EXPERIENCE)

@app.route('/certifications')
def certifications():
    return render_template('certifications.html',
        personal=PERSONAL, certifications=CERTIFICATIONS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        if name and email and message:
            flash(f'Thank you {name}! Your message has been received.', 'success')
        else:
            flash('Please fill in all required fields.', 'error')
        return redirect(url_for('contact'))
    return render_template('contact.html', personal=PERSONAL)

@app.route('/api/chat', methods=['POST'])
def chat_proxy():
    """Proxy Google Gemini API server-side (avoids CORS and protects the API key)."""
    if urlreq is None:
        return jsonify({'error': 'urllib not available'}), 500

    try:
        data = request.get_json(force=True)
        messages = data.get('messages') or []
        system = (data.get('system') or '').strip() or (
            'You are a helpful assistant for a personal portfolio site.')

        api_key = os.environ.get('GEMINI_API_KEY', '')
        if not api_key:
            return jsonify({'error': 'API key not configured'}), 500

        contents = []
        for m in messages:
            role = (m.get('role') or '').strip()
            content = (m.get('content') or '').strip()
            if not content:
                continue
            if role == 'user':
                contents.append({
                    'role': 'user',
                    'parts': [{'text': content}],
                })
            elif role == 'assistant':
                contents.append({
                    'role': 'model',
                    'parts': [{'text': content}],
                })

        if not contents:
            return jsonify({'error': 'No messages'}), 400

        payload_obj = {
            'contents': contents,
            'generationConfig': {
                'maxOutputTokens': 512,
                'temperature': 0.7,
            },
        }
        if system:
            payload_obj['systemInstruction'] = {'parts': [{'text': system}]}

        # Retries + fallback model (503s from urlopen become handled here, not shown raw)
        attempts = [
            ('gemini-2.5-flash', 0),
            ('gemini-2.5-flash', 1.3),
            ('gemini-2.0-flash', 0),
            ('gemini-2.0-flash', 1.3),
        ]
        last_err_msg = None
        for model, pause in attempts:
            if pause:
                time.sleep(pause)
            result, http_err = _gemini_generate_request(
                api_key, model, payload_obj)
            if http_err:
                _, msg = http_err
                last_err_msg = msg
                continue
            if 'error' in result:
                last_err_msg = (result.get('error') or {}).get(
                    'message', 'API error')
                continue
            text = _gemini_extract_text(result)
            if text:
                return jsonify({'content': [{'text': text}]})
            if _gemini_should_use_scope_reply(result):
                return jsonify({'content': [{'text': _CHAT_SCOPE_REPLY}]})
            return jsonify({'content': [{'text': _CHAT_SCOPE_REPLY}]})

        err_low = (str(last_err_msg) or '').lower()
        if any(
            x in err_low
            for x in ('503', 'unavailable', 'overload', '429', 'timeout', '500',
                      '502', 'bad gateway', 'connection')
        ):
            return jsonify({'content': [{'text': _CHAT_SERVICE_REPLY}]})
        return jsonify({'content': [{'text': _CHAT_SCOPE_REPLY}]})

    except Exception:
        return jsonify({'content': [{'text': _CHAT_SERVICE_REPLY}]})


if __name__ == '__main__':
    app.run(debug=True)

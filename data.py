"""
All site content lives here. Edit this file to update the portfolio —
templates and routes never contain personal data.

Image paths are relative to /static/.
"""

PERSONAL = {
    'name': 'Asad Mujeeb',
    'title': 'Data Analyst & BI Specialist',
    'tagline': 'Turning Raw Data Into Strategic Decisions',
    'summary': (
        'Data Analyst specializing in Business Intelligence, Machine Learning, '
        'and Analytics Engineering — building data systems that drive measurable, '
        'real-world outcomes.'
    ),
    'email': 'asadmujeeb559@gmail.com',
    'phone': '+92 316 6328876',
    'linkedin': 'https://linkedin.com/in/asadmujeeb',
    'linkedin_label': 'linkedin.com/in/asadmujeeb',
    'github': 'https://github.com/AsadMujeebAnalyst',
    'github_label': 'github.com/AsadMujeebAnalyst',
    'resume': '/static/Asad_Mujeeb_Resume.pdf',
    'location': 'Multan, Punjab, Pakistan',
    'locality': 'Multan',
    'region': 'Punjab',
    'country': 'PK',
    'photo': 'images/profile.webp',
    'status': 'Open to opportunities',
    'stats': [
        {'number': '2+', 'label': 'Years of experience'},
        {'number': '10+', 'label': 'Certifications'},
        {'number': '80%', 'label': 'Reporting automated'},
        {'number': '1M+', 'label': 'Data processed'},
    ],
}

ABOUT = [
    "I'm a **Data Analyst & Business Intelligence Specialist** based in Multan, Pakistan, "
    "passionate about transforming complex, messy data into clear, actionable insights that "
    "drive real business decisions.",

    "I specialize in building end-to-end analytics systems — not just dashboards, but scalable "
    "solutions that help organizations truly understand their performance and make confident decisions.",

    "Currently at [Dream Edge Technologies](https://www.topedgetechnologies.com/), I analyze mobile "
    "app performance and monetization metrics across a portfolio of 10+ apps. Using Firebase Analytics "
    "and GA4, I track user funnels, retention cohorts, ARPU, LTV, and subscription behavior at scale.",

    "Previously at [Blue Cascade Pakistan](https://bluecascade.org/), I designed and automated a lead "
    "generation system that delivered **300+ qualified B2B leads daily** with zero manual effort — "
    "significantly improving sales efficiency.",

    "My technical toolkit includes **SQL, Python, Power BI, Tableau, n8n, Selenium**, and "
    "**Machine Learning**. Whether it's data modeling, automation, or predictive analytics, I focus on "
    "delivering measurable business impact.",

    "Beyond professional work, I give back to the community as **Data Science Lead at The Youth Matrix** "
    "and as a **Microsoft Learn Student Ambassador**. I believe the real power of data lies in sharing "
    "knowledge and empowering others.",
]

# Grouped by what a hiring manager scans for.
SKILL_GROUPS = [
    {'name': 'Analysis & modelling',
     'items': ['Python', 'Pandas', 'SQL (MySQL)', 'Machine Learning', 'Statistical Analysis', 'Time Series']},
    {'name': 'BI & visualization',
     'items': ['Power BI', 'DAX', 'Tableau', 'Looker Studio', 'Excel']},
    {'name': 'Product analytics',
     'items': ['Google Analytics 4', 'Firebase', 'Funnels & cohorts', 'Retention & LTV']},
    {'name': 'Automation & engineering',
     'items': ['n8n', 'Selenium', 'REST APIs & webhooks', 'Flask', 'Git']},
]

BUSINESS_SKILLS = [
    'Translating data into actionable insights',
    'Stakeholder management & requirements gathering',
    'Root-cause & diagnostic analytics',
    'Data-driven decision support',
    'Funnel, cohort & retention analysis',
    'Executive reporting & data storytelling',
    'Cross-functional collaboration',
    'Data literacy coaching for teams',
]

# Add 'github': 'https://github.com/...' and/or 'demo': 'https://...' to any
# project and a labelled link appears on its card automatically.
PROJECTS = [
    {
        'id': 1,
        'title': 'Sales Performance Dashboard',
        'subtitle': 'Power BI · DAX · SQL Server',
        'description': 'Built an end-to-end Power BI solution analyzing sales across 5 regions. Engineered custom DAX measures for YoY growth, rolling averages, and territory ranking — delivered as a boardroom-ready executive report.',
        'impact': '15% increase in quarterly revenue decisions',
        'technologies': ['Power BI', 'DAX', 'SQL Server', 'Power Query'],
        'category': 'BI & Dashboards',
    },
    {
        'id': 2,
        'title': 'Customer Segmentation Engine',
        'subtitle': 'Python · Scikit-learn · Pandas',
        'description': 'Applied RFM modeling and K-Means clustering in Python to segment 50K+ customers. Integrated results into a marketing automation workflow that personalizes messaging per cluster.',
        'impact': '25% higher campaign conversion rate',
        'technologies': ['Python', 'Pandas', 'Scikit-learn', 'Matplotlib', 'Seaborn'],
        'category': 'Machine Learning',
    },
    {
        'id': 3,
        'title': 'Healthcare Readmission Analytics',
        'subtitle': 'Tableau · MySQL · Time Series',
        'description': 'Designed a Tableau workbook with time-series forecasting to identify high-risk patients pre-discharge. Built MySQL stored procedures feeding live data into the viz layer.',
        'impact': '25% reduction in 30-day readmission rates',
        'technologies': ['Tableau', 'MySQL', 'Time Series', 'Statistical Analysis'],
        'category': 'BI & Dashboards',
    },
    {
        'id': 4,
        'title': 'AI Calling Agent Lead Automation',
        'subtitle': 'n8n · Python · Selenium',
        'description': 'Automated lead generation and outreach for an AI calling agent using n8n workflows. The agent handles pre-proposal, post-proposal, and follow-up calls with leads generated through Google Ads.',
        'impact': '300+ leads/day automated — 0 manual effort',
        'technologies': ['n8n', 'Python', 'Selenium', 'Webhooks', 'REST APIs'],
        'category': 'Automation',
    },
    {
        'id': 5,
        'title': 'WhatsApp Chat Analyzer',
        'subtitle': 'Python · NLP · Streamlit',
        'description': 'Final year thesis — a Streamlit web app that parses WhatsApp exports and surfaces behavioral patterns: sentiment trends, activity heatmaps, top contributors, emoji frequency, and message volume forecasting.',
        'impact': 'Final year thesis project',
        'technologies': ['Python', 'NLP', 'Streamlit', 'Plotly', 'TextBlob'],
        'category': 'Machine Learning',
    },
    {
        'id': 6,
        'title': 'App Monetization KPI Tracker',
        'subtitle': 'GA4 · Firebase · Python',
        'description': 'Built a unified KPI framework in Python that pulls ARPU, ARPDAU, LTV, and retention cohorts from Firebase and GA4 APIs, then pushes aggregated metrics to a live Google Sheets dashboard for product teams.',
        'impact': 'Real-time monetization visibility for 10+ apps',
        'technologies': ['Firebase', 'Google Analytics 4', 'Python', 'Google Sheets API'],
        'category': 'Analytics Engineering',
    },
]

EXPERIENCE = [
    {
        'title': 'Data Analyst (Games & Apps)',
        'company': 'Dream Edge Technologies',
        'logo': 'images/det_logo.png',
        'company_website': 'https://topedgetechnologies.com/',
        'linkedin_url': 'https://www.linkedin.com/company/dream-edge-technologies',
        'type': 'Full-time',
        'period': 'Mar 2026 — Present',
        'current': True,
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
        'logo': 'images/bcc_logo.png',
        'company_website': 'https://bluecascade.org/',
        'linkedin_url': 'https://www.linkedin.com/company/blue-cascade/',
        'type': 'Full-time',
        'period': 'Mar 2025 — Mar 2026',
        'current': False,
        'location': 'Onsite',
        'responsibilities': [
            'Worked on an AI Calling Agent using n8n and built end-to-end data pipelines for it',
            'Full-stack development using Python, Flask, and MySQL for internal business tools',
            'Led BI initiatives for executive reporting, building Power BI dashboards for C-suite decision-making',
            'Implemented Google Analytics event tracking for e-commerce order and funnel analysis',
        ],
        'tools': ['n8n', 'Python', 'PostgreSQL', 'Power BI', 'Looker Studio', 'Database Architecture'],
    },
    {
        'title': 'Business Intelligence Analyst',
        'company': 'Ai NEURALZ',
        'logo': 'images/ai_neuralz_logo.jpg',
        'company_website': None,
        'linkedin_url': 'https://www.linkedin.com/company/ai-neuralz/',
        'type': 'Full-time',
        'period': 'May 2024 — Oct 2024',
        'current': False,
        'location': 'Onsite',
        'responsibilities': [
            'Built a real-time Looker dashboard for streaming platform HdHub4u, presented to stakeholders',
            'Developed interactive Power BI dashboards serving sales and marketing teams',
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
        'type': 'Job simulation',
        'period': 'Jun 2024 — Jul 2024',
        'current': False,
        'location': 'Online',
        'responsibilities': [
            'Advised a hypothetical social media client as a Data Analyst at Accenture',
            'Cleaned, modeled, and analyzed 7 datasets to uncover insights into content trends',
            'Prepared a boardroom PowerPoint deck and video presentation for client and internal stakeholders',
        ],
        'tools': ['Power BI', 'Excel', 'PowerPoint', 'Data Modeling'],
    },
]

# credential_id is only shown when set. Add the real ID from each
# certificate page where you have it.
CERTIFICATIONS = [
    {
        'name': 'Business Intelligence',
        'issuer': 'Google',
        'date': 'Aug 2024',
        'credential_id': 'CDJXZEZG0NVD',
        'description': 'Expertise in preparing, modeling, visualizing and analyzing data. Advanced DAX, Power Query, and data model design using Microsoft Power BI.',
        'skills': ['Power BI', 'DAX', 'Power Query', 'Data Modeling'],
        'verify_url': 'https://www.coursera.org/account/accomplishments/professional-cert/CDJXZEZG0NVD',
    },
    {
        'name': 'Machine Learning with Python',
        'issuer': 'freeCodeCamp',
        'date': 'Jul 2023',
        'credential_id': None,
        'description': 'Hands-on experience with supervised & unsupervised learning, neural networks, and data preprocessing pipelines.',
        'skills': ['Data Preprocessing', 'Feature Engineering', 'Model Building', 'Hyperparameter Tuning'],
        'verify_url': 'https://www.freecodecamp.org/certification/AsadMujeeb/machine-learning-with-python-v7',
    },
    {
        'name': 'Data Analyst Track',
        'issuer': 'DataCamp',
        'date': '2022',
        'credential_id': None,
        'description': 'Comprehensive data analysis techniques, predictive modeling, and statistical methods for extracting insights at scale.',
        'skills': ['NumPy', 'Pandas', 'Matplotlib', 'Seaborn'],
        'verify_url': 'https://www.datacamp.com/completed/statement-of-accomplishment/track/89e4b7150c0fca83684be3b236c24b27181505fe',
    },
    {
        'name': 'SQL Track',
        'issuer': 'Codecademy',
        'date': 'Jul 2024',
        'credential_id': None,
        'description': 'Proficient in SQL for data querying, database design, optimization, and complex multi-table joins and aggregations.',
        'skills': ['Data Query', 'Database Design', 'Data Manipulation', 'Aggregation & Joins'],
        'verify_url': 'https://www.codecademy.com/profiles/Asad-Mujeeb/certificates/042a4e5884e3eb6ea1f2a12be6abb851',
    },
]

AWARDS = [
    {
        'image': 'images/award_youth_matrix.webp',
        'title': 'Technical Leadership Award 2025',
        'org': 'The Youth Matrix',
        'alt': 'Glass trophy: Technical Leadership Award 2025 presented to Asad Mujeeb by The Youth Matrix',
        'width': 433, 'height': 577,
    },
    {
        'image': 'images/award_blue_cascade.webp',
        'title': 'Recognition for dedication and consistent effort',
        'org': 'Blue Cascade · AI Team',
        'alt': 'Glass recognition plaque from Blue Cascade awarded to Asad Mujeeb, AI Team',
        'width': 331, 'height': 754,
    },
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
        'announcement': 'images/the_youth_matrix_announcement.webp',
        'group_photo': 'images/the_youth_matrix_group_photo.webp',
        'announcement_size': (900, 1125),
        'group_size': (1400, 1050),
    },
    {
        'org': 'Microsoft Learn Student Ambassadors',
        'slug': 'mlsa',
        'role': 'Data Analytics Lead',
        'period': 'Aug 2024 — Apr 2025',
        'description': 'Represented Microsoft’s student program locally — hosting workshops, supporting peers with data analytics tooling, and helping onboard new ambassadors to the community.',
        'achievements': [
            'Led sessions and study jams on Power BI, Excel, and storytelling with data for student audiences',
            'Mentored participants through hands-on analytics challenges and presentation best practices',
            'Contributed to community events that connect learners with cloud and modern workplace skills',
        ],
        'logo': 'images/mlsa_logo.webp',
        'announcement': 'images/mlsa_announcement.webp',
        'group_photo': 'images/mlsa_group_photo.webp',
        'announcement_size': (720, 902),
        'group_size': (1400, 1050),
    },
]

EDUCATION = [
    {
        'degree': 'Bachelor of Information & Communication Technology',
        'institution': 'Bahauddin Zakariya University (BZU)',
        'institution_url': 'https://bzu.edu.pk/',
        'location': 'Multan, Pakistan',
        'period': '2021 — 2025',
        'gpa': '3.56 / 4.0',
        'thesis': 'WhatsApp Chat Analyzer',
        'thesis_summary': (
            'A Python + NLP Streamlit application that analyzes exported WhatsApp chats to uncover '
            'sentiment trends, activity patterns, top contributors, and message volume forecasts.'
        ),
    }
]

# (label, endpoint) — order = navigation order
NAV = [
    ('About', 'about'),
    ('Experience', 'experience'),
    ('Projects', 'projects'),
    ('Certifications', 'certifications'),
    ('Community', 'volunteer'),
    ('Contact', 'contact'),
]

"""
Static site generator — renders each Flask route to HTML in dist/.
Run: python build.py
"""
import os
import shutil
from app import app

ROUTES = [
    ('/', 'index.html'),
    ('/about', 'about/index.html'),
    ('/volunteer', 'volunteer/index.html'),
    ('/projects', 'projects/index.html'),
    ('/experience', 'experience/index.html'),
    ('/certifications', 'certifications/index.html'),
    ('/contact', 'contact/index.html'),
]

DIST = 'dist'

def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    # Copy static assets
    if os.path.exists('static'):
        shutil.copytree('static', os.path.join(DIST, 'static'))

    with app.test_client() as client:
        for route, output_path in ROUTES:
            response = client.get(route)
            if response.status_code != 200:
                print(f'WARNING: {route} returned {response.status_code}')
            html = response.data.decode('utf-8')
            out_file = os.path.join(DIST, output_path)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'Built {route} → {out_file}')

    print(f'\nDone. Output: {DIST}/')

if __name__ == '__main__':
    build()

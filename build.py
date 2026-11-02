"""
Static site generator — renders each Flask route to HTML in dist/.
Run: python build.py
"""
import os
import shutil

from app import SITE_URL, app

# (route, output file, include in sitemap)
ROUTES = [
    ('/', 'index.html', True),
    ('/about', 'about/index.html', True),
    ('/experience', 'experience/index.html', True),
    ('/projects', 'projects/index.html', True),
    ('/certifications', 'certifications/index.html', True),
    ('/volunteer', 'volunteer/index.html', True),
    ('/contact', 'contact/index.html', True),
    ('/thank-you', 'thank-you/index.html', False),
    ('/404', '404.html', False),
]

DIST = 'dist'


def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    shutil.copytree('static', os.path.join(DIST, 'static'))

    failed = False
    with app.test_client() as client:
        for route, output_path, _ in ROUTES:
            response = client.get(route)
            if response.status_code != 200:
                print(f'ERROR: {route} returned {response.status_code}')
                failed = True
                continue
            out_file = os.path.join(DIST, output_path)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(response.data.decode('utf-8'))
            print(f'Built {route} -> {out_file}')

    # robots.txt + sitemap.xml (the sitemap needs an absolute URL)
    robots = ['User-agent: *', 'Allow: /', 'Disallow: /thank-you/']
    if SITE_URL:
        robots.append(f'Sitemap: {SITE_URL}/sitemap.xml')
        urls = ''.join(
            f'  <url><loc>{SITE_URL}{route.rstrip("/")}/</loc></url>\n'
            for route, _, in_sitemap in ROUTES if in_sitemap)
        with open(os.path.join(DIST, 'sitemap.xml'), 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                    f'{urls}</urlset>\n')
        print('Built sitemap.xml')
    else:
        print('NOTE: SITE_URL/URL not set — skipping sitemap.xml and absolute canonical/OG URLs.')
    with open(os.path.join(DIST, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(robots) + '\n')

    if failed:
        raise SystemExit(1)
    print(f'\nDone. Output: {DIST}/')


if __name__ == '__main__':
    build()

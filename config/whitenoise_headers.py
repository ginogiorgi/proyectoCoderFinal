def set_custom_headers(headers, path, url):
    if path.endswith('.css') or path.endswith('.js'):
        ct = headers.get('Content-Type', '')
        if 'charset' not in ct:
            headers['Content-Type'] = ct + '; charset=utf-8' if ct else 'text/css; charset=utf-8'
    # Set Cache-Control for all static files (1 year, immutable)
    headers['Cache-Control'] = 'public, max-age=31536000, immutable'

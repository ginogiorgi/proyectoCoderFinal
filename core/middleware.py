class MediaCacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/media/'):
            response['Cache-Control'] = 'public, max-age=604800'  # 1 week
            # Remove X-Frame-Options if present
            if 'X-Frame-Options' in response:
                del response['X-Frame-Options']
        return response

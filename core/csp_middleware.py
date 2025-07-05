class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        # Permite solo tu dominio y ninguno más (ajusta si necesitas permitir otros)
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' https://cdn.jsdelivr.net https://ajax.googleapis.com https://unpkg.com; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://unpkg.com; "
            "img-src 'self' data: https://cdn.jsdelivr.net https://unpkg.com; "
            "font-src 'self' https://cdn.jsdelivr.net https://unpkg.com; "
            "frame-ancestors 'self'; "
        )
        return response

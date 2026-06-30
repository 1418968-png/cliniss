from django.conf import settings


class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault('Content-Security-Policy', self.content_security_policy())
        response.setdefault(
            'Permissions-Policy',
            'camera=(), geolocation=(), microphone=(), payment=(), usb=()',
        )
        response.setdefault('Cross-Origin-Opener-Policy', 'same-origin')
        return response

    @staticmethod
    def content_security_policy():
        directives = [
            "default-src 'self'",
            "script-src 'self'",
            "style-src 'self' 'unsafe-inline'",
            "img-src 'self' data: https://*.yandex.ru https://*.yandex.net https://yastatic.net",
            "font-src 'self' data:",
            "frame-src https://yandex.ru https://*.yandex.ru",
            "connect-src 'self'",
            "base-uri 'self'",
            "form-action 'self'",
            "frame-ancestors 'none'",
            "object-src 'none'",
        ]
        if settings.CSP_UPGRADE_INSECURE_REQUESTS:
            directives.append('upgrade-insecure-requests')
        return '; '.join(directives)

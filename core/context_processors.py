from .site import NAVIGATION, SITE


def site_context(request):
    path = request.path.strip('/')
    language = 'en' if path == 'en' or path.endswith('-en') else 'ru'
    return {
        'site': SITE,
        'navigation': NAVIGATION.get(language, NAVIGATION['ru']),
        'current_language': language,
    }

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.utils import timezone

from .data import PAGE_ORDER, PAGES, get_page, search_pages


def _redirect_without_trailing_slash(request, path):
    query = request.GET.urlencode()
    target = path
    if query:
        target = f'{target}?{query}'
    return HttpResponsePermanentRedirect(target)


def page_detail(request, slug=''):
    page = get_page(slug)
    if page is None:
        raise Http404('Page not found')
    return render(request, 'pages/detail.html', {'page': page})


def page_detail_trailing_slash(request, slug):
    page = get_page(slug)
    if page is None:
        raise Http404('Page not found')
    return _redirect_without_trailing_slash(request, f'/{slug}')


def search_trailing_slash(request):
    return _redirect_without_trailing_slash(request, '/search')


def search(request):
    query = request.GET.get('q', '').strip()
    results = search_pages(query) if query else []
    return render(request, 'pages/search.html', {'query': query, 'results': results})


def favicon_ico(request):
    favicon_path = settings.BASE_DIR / 'static' / 'site' / 'img' / 'favicon.ico'
    return FileResponse(favicon_path.open('rb'), content_type='image/x-icon')


def service_worker_js(request):
    response = HttpResponse(
        """
self.addEventListener('install', function (event) {
    self.skipWaiting();
});

self.addEventListener('activate', function (event) {
    event.waitUntil(self.registration.unregister());
});
""".strip(),
        content_type='application/javascript; charset=utf-8',
    )
    response['Cache-Control'] = 'no-store, max-age=0'
    return response


def robots_txt(request):
    body = '\n'.join(
        [
            'User-Agent: *',
            'Disallow: /admin/',
            'Disallow: /cliniss/',
            '',
            f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
            '',
        ]
    )
    return HttpResponse(body, content_type='text/plain; charset=utf-8')


def sitemap_xml(request):
    base_url = request.build_absolute_uri('/').rstrip('/')
    lastmod = timezone.localdate().isoformat()
    urls = []
    for slug in PAGE_ORDER:
        path = '/' if slug == '' else f'/{slug}'
        urls.append(
            f'  <url><loc>{base_url}{path}</loc><lastmod>{lastmod}</lastmod></url>'
        )
    body = '\n'.join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            *urls,
            '</urlset>',
            '',
        ]
    )
    return HttpResponse(body, content_type='application/xml; charset=utf-8')

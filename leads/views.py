from ipaddress import ip_address
from urllib.parse import urlsplit, urlunsplit

from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.crypto import salted_hmac
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import LeadForm


def normalize_ip(value):
    if not value:
        return None
    try:
        return str(ip_address(value.strip()))
    except ValueError:
        return None


def get_client_ip(request):
    if settings.TRUST_X_FORWARDED_FOR:
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
        for candidate in forwarded_for.split(','):
            parsed = normalize_ip(candidate)
            if parsed:
                return parsed
    return normalize_ip(request.META.get('REMOTE_ADDR'))


def is_safe_url(request, url):
    return url_has_allowed_host_and_scheme(
        url,
        allowed_hosts={request.get_host()},
        require_https=not settings.DEBUG,
    )


def safe_next_url(request):
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('pages:home')
    if not is_safe_url(request, next_url):
        return reverse('pages:home')
    return next_url


def source_path(request):
    raw_path = request.POST.get('next') or request.META.get('HTTP_REFERER', '')
    if not raw_path or not is_safe_url(request, raw_path):
        return ''

    parsed = urlsplit(raw_path)
    path = parsed.path or '/'
    if parsed.query:
        path = f'{path}?{parsed.query}'
    return path[:255]


def with_lead_fragment(url):
    parsed = urlsplit(url)
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, 'lead-form'))


def lead_rate_limited(request):
    max_attempts = settings.LEAD_RATE_LIMIT_MAX_ATTEMPTS
    if max_attempts <= 0:
        return False

    window = settings.LEAD_RATE_LIMIT_WINDOW_SECONDS
    identity = get_client_ip(request) or request.META.get('REMOTE_ADDR') or 'unknown'
    digest = salted_hmac('lead-rate-limit', identity).hexdigest()
    key = f'lead-submit:{digest}'
    attempts = cache.get(key, 0)
    if attempts >= max_attempts:
        return True

    if not cache.add(key, 1, timeout=window):
        try:
            cache.incr(key)
        except ValueError:
            cache.set(key, 1, timeout=window)
    return False


@require_POST
def submit_lead(request):
    next_url = safe_next_url(request)
    if lead_rate_limited(request):
        messages.error(request, 'Слишком много заявок. Попробуйте отправить форму позже.')
        return redirect(with_lead_fragment(next_url))

    form = LeadForm(request.POST)

    if form.is_valid():
        lead = form.save(commit=False)
        lead.source_path = source_path(request)
        lead.user_agent = request.META.get('HTTP_USER_AGENT', '')
        lead.ip_address = get_client_ip(request)
        lead.save()
        messages.success(request, 'Заявка сохранена. Мы свяжемся с вами после обработки.')
    else:
        messages.error(request, 'Проверьте форму: имя, телефон и согласие обязательны.')

    return redirect(with_lead_fragment(next_url))

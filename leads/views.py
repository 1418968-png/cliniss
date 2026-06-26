from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import LeadForm


def get_client_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


@require_POST
def submit_lead(request):
    form = LeadForm(request.POST)
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('pages:home')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = reverse('pages:home')

    if form.is_valid():
        lead = form.save(commit=False)
        lead.source_path = request.POST.get('next') or request.META.get('HTTP_REFERER', '')
        lead.user_agent = request.META.get('HTTP_USER_AGENT', '')
        lead.ip_address = get_client_ip(request)
        lead.save()
        messages.success(request, 'Заявка сохранена. Мы свяжемся с вами после обработки.')
    else:
        messages.error(request, 'Проверьте форму: имя, телефон и согласие обязательны.')

    if '#lead-form' not in next_url:
        next_url = f'{next_url}#lead-form'
    return redirect(next_url)

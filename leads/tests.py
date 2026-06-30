from django.core.cache import cache
from django.test import TestCase, override_settings

from .models import Lead


class LeadFormTests(TestCase):
    def setUp(self):
        cache.clear()

    def lead_payload(self, **overrides):
        payload = {
            'lead_type': Lead.LeadType.PROPOSAL,
            'language': Lead.Language.RU,
            'name': 'Тестовый пользователь',
            'phone': '+7 900 000-00-00',
            'email': 'test@example.com',
            'message': 'Нужна консультация',
            'consent': 'on',
            'next': '/',
        }
        payload.update(overrides)
        return payload

    def test_submit_lead_creates_record(self):
        response = self.client.post(
            '/leads/submit',
            self.lead_payload(),
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Lead.objects.count(), 1)
        lead = Lead.objects.get()
        self.assertEqual(lead.name, 'Тестовый пользователь')
        self.assertEqual(lead.lead_type, Lead.LeadType.PROPOSAL)

    def test_honeypot_field_rejects_bot_submission(self):
        response = self.client.post(
            '/leads/submit',
            self.lead_payload(website='https://spam.example'),
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Lead.objects.count(), 0)

    def test_forwarded_for_is_ignored_until_trusted(self):
        response = self.client.post(
            '/leads/submit',
            self.lead_payload(),
            REMOTE_ADDR='127.0.0.1',
            HTTP_X_FORWARDED_FOR='203.0.113.10',
        )

        self.assertEqual(response.status_code, 302)
        lead = Lead.objects.get()
        self.assertEqual(lead.ip_address, '127.0.0.1')

    @override_settings(LEAD_RATE_LIMIT_MAX_ATTEMPTS=1, LEAD_RATE_LIMIT_WINDOW_SECONDS=600)
    def test_rate_limit_blocks_repeated_submissions(self):
        first = self.client.post('/leads/submit', self.lead_payload())
        second = self.client.post('/leads/submit', self.lead_payload(name='Другой пользователь'))

        self.assertEqual(first.status_code, 302)
        self.assertEqual(second.status_code, 302)
        self.assertEqual(Lead.objects.count(), 1)

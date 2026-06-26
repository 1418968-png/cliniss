from django.test import TestCase

from .models import Lead


class LeadFormTests(TestCase):
    def test_submit_lead_creates_record(self):
        response = self.client.post(
            '/leads/submit',
            {
                'lead_type': Lead.LeadType.PROPOSAL,
                'language': Lead.Language.RU,
                'name': 'Тестовый пользователь',
                'phone': '+7 900 000-00-00',
                'email': 'test@example.com',
                'message': 'Нужна консультация',
                'consent': 'on',
                'next': '/',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Lead.objects.count(), 1)
        lead = Lead.objects.get()
        self.assertEqual(lead.name, 'Тестовый пользователь')
        self.assertEqual(lead.lead_type, Lead.LeadType.PROPOSAL)

# Create your tests here.

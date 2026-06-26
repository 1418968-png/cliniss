from django.test import TestCase
from django.contrib.staticfiles import finders

from .data import PAGE_ORDER, PAGES


class PageRouteTests(TestCase):
    def test_public_pages_return_success(self):
        for slug in PAGE_ORDER:
            with self.subTest(slug=slug):
                path = '/' if slug == '' else f'/{slug}'
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)

    def test_service_files_return_success(self):
        for path in ['/robots.txt', '/sitemap.xml', '/favicon.ico', '/service-worker.js']:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)

    def test_public_pages_with_trailing_slash_redirect_to_canonical_urls(self):
        for slug in PAGE_ORDER:
            if slug == '':
                continue
            with self.subTest(slug=slug):
                response = self.client.get(f'/{slug}/')
                self.assertEqual(response.status_code, 301)
                self.assertEqual(response['Location'], f'/{slug}')

    def test_search_with_trailing_slash_redirects_and_preserves_query(self):
        response = self.client.get('/search/?q=доброволец')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], '/search?q=%D0%B4%D0%BE%D0%B1%D1%80%D0%BE%D0%B2%D0%BE%D0%BB%D0%B5%D1%86')

    def test_structured_sections_do_not_leak_python_dict_items(self):
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "('title',")
        self.assertNotContains(response, "('body',")

    def test_contacts_include_map_and_reception_hours(self):
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CLINISS на карте')
        self.assertContains(response, '10:00-13:00')
        self.assertContains(response, 'map-widget')

    def test_docs_include_downloadable_policy_and_consent_links(self):
        response = self.client.get('/docs')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Политика об обработке персональных данных')
        self.assertContains(response, 'Информированное добровольное согласие')
        self.assertContains(response, 'https://disk.yandex.ru/i/zNO3XYku2JzNeg')
        self.assertContains(response, 'https://disk.yandex.ru/i/oEXu78YjBmLc4g')

    def test_contextual_lead_types_are_selected(self):
        checks = [
            ('/volunteers', 'volunteer', 'Анкета добровольца'),
            ('/contacts', 'question', 'Задать вопрос'),
            ('/price', 'proposal', 'Запросить коммерческое предложение'),
            ('/employees', 'team', 'Стать частью команды'),
        ]
        for path, value, label in checks:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(
                    response,
                    f'<option value="{value}" selected>{label}</option>',
                    html=True,
                )

    def test_page_image_assets_exist(self):
        paths = set()
        for page in PAGES.values():
            if page.get('hero_image'):
                paths.add(page['hero_image'])
            for section in page['sections']:
                image = section.get('image')
                if image:
                    paths.add(image['src'])
                for image in section.get('images', []):
                    paths.add(image['src'])
                for card in section.get('cards', []):
                    if card.get('image'):
                        paths.add(card['image'])

        for path in sorted(paths):
            with self.subTest(path=path):
                self.assertIsNotNone(finders.find(path), path)

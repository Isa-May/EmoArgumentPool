from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_is_url_accessible_via_name(self):
        response = self.client.get(reverse("render_arguments"))
        self.assertEqual(response.status_code, 200)
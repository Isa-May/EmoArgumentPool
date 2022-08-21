from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse


class HomepageTests(TestCase):
    def test_is_url_accessible_via_name(self):
        response = self.client.get(reverse("render_arguments"))
        self.assertEqual(response.status_code, 200)

    def test_if_url_location_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

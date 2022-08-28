from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client

# Create your tests here.
from django.urls import reverse

from simpleDataViewer.models import EmoArgument

c = Client()

class HomepageTests(TestCase):
    def test_is_argument_emo(self):
        """test whether the retrieved arguments are in fact the emotional ones"""
        response = self.client.get(reverse("render_arguments_by_topic_1"))
        # check whether the response arguments are the same as the ones with label 1 in the database (the emotional ones)
        database_emo = EmoArgument.objects.all().filter(topic='firefox-vs-internet-explorer', label=0)
        self.assertEqual(response, database_emo)

    def test_is_url_accessible_via_name(self):
        response = self.client.get(reverse("render_arguments_by_topic_1"))
        self.assertEqual(response.status_code, 200)

    def test_if_url_location_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse
import os
from django.conf import settings


# Create your tests here.

class HomePageLoadingTest(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_home_page_load_fully_success(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")
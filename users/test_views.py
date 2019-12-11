from django.test import TestCase
from django.shortcuts import get_list_or_404

class TestViews(TestCase):
    def test_get_login(self):
        page = self.client.get("/users/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    def test_registration_page(self):
        page = self.client.get("/users/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    def test_profile_page(self):
        page = self.client.get("/users/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
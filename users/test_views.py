from django.test import TestCase
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User

class TestLogin(TestCase):
    def test_get_login(self):
        page = self.client.get("/users/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

class TestProfile(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing", email="testing@outlook.com")
        self.client.login(username="test", password="testing")
                    
    def test_profile_page(self):
        page = self.client.get("/users/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
class TestRegistration(TestCase):
    def test_registration_page(self):
        page = self.client.get("/users/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
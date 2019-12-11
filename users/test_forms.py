from django.test import TestCase
from django.contrib.auth.models import User
from .forms import LoginForm

class TestLoginForm(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing", email="testing@outlook.com")
        self.client.login(username="test", password="testing")
    
    def test_login_form(self):
        form = LoginForm({'username': 'test'}, {'password': 'testing'})
        self.assertFalse(form.is_valid())
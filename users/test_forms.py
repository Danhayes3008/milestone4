from django.test import TestCase
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from webbrowser import get

class TestLoginForm(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing", email="testing@outlook.com")
        self.client.login(username="test", password="testing")
    
    def test_login_form(self):
        form = LoginForm({'username': 'test'}, {'password': 'testing'})
        self.assertFalse(form.is_valid())
        
class TestRegistrationForm(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing", 
                                        email="testing@outlook.com")
        self.client.login(username="test", password="testing")
        
    def test_users_can_register(self):
        form = RegistrationForm({'username': 'test'}, {'password': 'testing'}, 
                                {'email': 'testing@outlook.com'})
        self.assertFalse(form.is_valid())
    
    def test_clean_email(self):
        email = RegistrationForm({'username': 'test'}, {'password': 'testing'}, {'email': 'testing@outlook.com'})
        self.assertFalse(email.is_valid())
         
    def test_email_cant_be_left_blank(self):
        def setUp(self):
            user = User.objects.create_user(username="test", password="testing", 
                                        email="")
        email = RegistrationForm({'username': 'test', 'password':'testing', 'email': ''})
        self.assertFalse(email.is_valid())
        self.assertEqual(email.errors['email'], ['This field is required.'])

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import LoginForm, RegistrationForm

# This def will show us the index.html page 
def index(request):
    return render(request, 'index.html')
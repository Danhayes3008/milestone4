from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import LoginForm, RegistrationForm

# This def will show us the index.html page 
def index(request):
    return render(request, 'index.html')

# This def creates the login capability and uses the login form from the forms.py file

def Login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "Welcome to Help the Homeless!")
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Incorrect username or password, please try again.")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})
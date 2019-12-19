from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import LoginForm, RegistrationForm, UserForm, ProfileForm

# This def creates the login capability and uses the login form from the forms.py file

def login(request):
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

# This section deals with the logout function

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Thank you for visiting, please come again")
    return redirect(reverse('index'))

# this section contains the registration def used to allow new users to register an account

def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)  
              
        if registration_form.is_valid():
            registration_form.save() 
                       
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome to Help the Homless")
            else:
                messages.error(request, "Something went wrong, please try again")
    else:
        registration_form = RegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})
def profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
def update(request):
    return render(request, 'update.html')

@login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile.html')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
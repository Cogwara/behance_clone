from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('user_profile')  # Redirect to your profile
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('user_profile')  # Redirect to your homepage
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'accounts/logout.html') 


@login_required
def user_profile(request):
    # Retrieve the user's profile data
    user = request.user

    # Render the user profile page with the user's data
    return render(request, 'accounts/user_profile.html', {'user': user})

@login_required
def profile_update(request):
    user_profile = request.user.userprofile 

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the profile page after a successful update
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'accounts/profile_update.html', {'form': form})

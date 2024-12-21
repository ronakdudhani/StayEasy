from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django import forms
from django.contrib import messages
from property.models import Property



def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('home')

    return render(request, 'users/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')  # Redirect to home or a specific page
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

@login_required
def settings_view(request):
    return render(request, 'users/settings.html')


@login_required  # Ensure the user is logged in
def user_properties(request):
    # Get properties added by the logged-in user
    properties = Property.objects.filter(user=request.user)
    return render(request, 'users/user_properties.html', {'properties': properties})




# Custom form for updating user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

# Settings View
@login_required
def settings_view(request):
    user = request.user

    # Handle profile update form
    profile_form = ProfileUpdateForm(instance=user)
    if request.method == 'POST' and 'update_profile' in request.POST:
        profile_form = ProfileUpdateForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('users:settings')

    # Handle password change form
    password_form = PasswordChangeForm(user)
    if request.method == 'POST' and 'update_password' in request.POST:
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            messages.success(request, "Password changed successfully!")
            return redirect('users:settings')

    return render(request, 'users/settings.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


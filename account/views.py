from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, ProfileForm
from account.models import Profile


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if hasattr(user, 'profile'):
                    login(request, user)
                    return redirect('homepage')
                else:
                    return redirect('create_profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def create_profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('homepage')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def account(request):
        return render(request, 'create_profile.html')

def homepage(request):
    return render(request, 'homepage.html')
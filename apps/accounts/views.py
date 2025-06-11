from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        user_form = AuthenticationForm(request, data=request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            return redirect('index')
    else:
        user_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': user_form})

def register_view(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile_view(request):
    try:
        if request.user.is_authenticated:
            profile_info = Profile.objects.get(user = request.user.id)
            return render(request, 'accounts/profile.html', {'profile': profile_info})
        else:
            return redirect('index')
    except Profile.DoesNotExist:    
        return render(request, 'not_found.html')

def logout_view(request):
    logout(request)
    return redirect('index')



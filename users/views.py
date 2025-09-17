import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()


# Render registration form & handle user creation
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('attendance_dashboard')

    return render(request, 'users/register.html')


# Render login form & authenticate user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('attendance_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'users/login.html')


# Logout and redirect
def logout_user(request):
    logout(request)
    return redirect('login')


# Protected dashboard view (example)
@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {'user': request.user})

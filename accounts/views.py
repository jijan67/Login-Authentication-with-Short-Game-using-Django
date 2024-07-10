from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = Customer.objects.get(name=name)
            except Customer.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html', {'user': request.user})


def profile(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            request.user.profile_image = profile_image
            request.user.save()
            messages.success(request, 'Profile image updated successfully!')
        else:
            messages.error(request, 'No file selected!')

    # Pass the user object to the template context
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')


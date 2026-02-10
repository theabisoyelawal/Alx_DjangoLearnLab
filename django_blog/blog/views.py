from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Profile view for authenticated users
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return render(request, 'blog/profile.html', {'user': request.user})

    def post(self, request):
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return render(request, 'blog/profile.html', {'user': user, 'success': True})

# Simple login view
class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        return render(request, 'blog/login.html', {'error': 'Invalid credentials'})

# Simple register view
class RegisterView(View):
    def get(self, request):
        return render(request, 'blog/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('login')
        return render(request, 'blog/register.html', {'error': 'Username already exists'})

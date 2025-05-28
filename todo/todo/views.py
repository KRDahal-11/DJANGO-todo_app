from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login


def signup(request):
    if request.method == 'POST':
        user=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')

        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        if User.objects.filter(username=user).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        
        try:
            print(user, email, password2)
            # Create a new user
            new_user = User.objects.create_user(username=user, password=password2, email=email)
            new_user.save()
            # Optionally, redirect to a success page or login page
            return redirect('/login')
        except Exception as e:
            print(f"Error creating user: {e}")
            return render(request, 'signup.html', {'error': 'An error occurred while creating the account'})
    else:
        return render(request, 'signup.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/todo')  # Redirect to the todo page or any other page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def todo(request):
    return render(request, 'todo.html')
                 
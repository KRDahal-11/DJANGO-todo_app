from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import get_object_or_404



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

# def todo(request):
#     if not request.user.is_authenticated:
#         return redirect('/login')
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         if title:
#             TODOO.objects.create(title=title, user=request.user)
#             return redirect('/todo')
#     todos = TODOO.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'todo.html', {'todos': todos})

def todo(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        action = request.POST.get('action')
        todo_id = request.POST.get('todo_id')
        if action == 'edit' and todo_id:
            new_title = request.POST.get('new_title')
            todo_item = get_object_or_404(TODOO, id=todo_id, user=request.user)
            if new_title:
                todo_item.title = new_title
                todo_item.save()
        elif action == 'delete' and todo_id:
            todo_item = get_object_or_404(TODOO, id=todo_id, user=request.user)
            todo_item.delete()
        else:
            # Add new todo
            title = request.POST.get('title')
            if title:
                TODOO.objects.create(title=title, user=request.user)
        return redirect('/todo')
    todos = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'todos': todos})




                 
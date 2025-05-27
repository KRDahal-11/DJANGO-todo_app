from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
def signup(request):
    if request.method == 'POST':
        user=request.POST.get('username')
        password=request.POST.get('password2')
        email=request.POST.get('email')
        print(user, email, password)

    return render(request, 'signup.html')
                 
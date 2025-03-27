from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import time


# Create your views here.
def login_users(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            
        else:
            messages.success(request, "There was an error login in")
            time.sleep(3)
            messages
            return redirect('login')

    else:       
        return render(request, 'members/login.html')

def logout_user(request):
    logout(request)
    return redirect('hero')
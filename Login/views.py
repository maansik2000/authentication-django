from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account is created for '+ user)
                
                return redirect('login')
            
        context = {'form' : form}
        return render(request,'Login/register.html',context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request,'Login/login.html',context )


@login_required(login_url='login')
def home(request):
    context = {}
    
    return render(request,'Login/home.html',context )

def logoutUser(request):
    logout(request)
    return redirect('login')
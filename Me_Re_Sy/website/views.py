from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpFrom
# Create your views here.


def home(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Bem vindo!")
            return redirect('home')
        else:
            messages.success(request,'Incorrect password or username')
            return redirect('home')
    else:
        return render(request, 'home.html',{})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.info(request, "See ya")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form= SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,f"Account created for {username}. You are now logged in.")
            return redirect('home')  
    else: 
        form=SignUpFrom()
        return render(request, 'register.html',{'form' :form})
    return render(request, 'register.html',{'form' :form})
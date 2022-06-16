from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user= auth.authenticate(req, username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('home')
        else:
            return render(req, 'bad_login.html')
    else:
        return render(req, 'login.html')

def logout(req):
    auth.logout(req)
    return redirect('home')

def sign_up(req):
    if req.method == 'POST':
        if req.POST['password'] == req.POST['repeat']:
            new_user = User.objects.create_user(username=req.POST['username'], password=req.POST['password'])
            auth.login(req, new_user)
            return redirect('home')
    return render(req, 'register.html')
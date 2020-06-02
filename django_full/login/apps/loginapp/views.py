from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
import bcrypt

from .models import User

def index(request):
    return render(request, "loginapp/index.html")

def regester(request):
    errors= User.objects.user_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        encrypted = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        registerate = User.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], email= request.POST['email'], dob= request.POST['dob'], password= encrypted)
        request.session['userid'] = User.objects.get(email= request.POST['email']).id
        return redirect("/success")

def login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        request.session['userid'] = User.objects.get(email= request.POST['email']).id
        return redirect("/success")

def success(request):
    if 'userid' not in request.session:
        return redirect ("/")

    context={
        "userid":User.objects.get(id=request.session['userid'])
    }
    return render(request, "loginapp/success.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")
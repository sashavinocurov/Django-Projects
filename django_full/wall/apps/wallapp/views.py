from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
import bcrypt

from .models import User, Message, Comment

def index(request):
    return render(request, "wallapp/login.html")

def wall(request):
    if 'userid' not in request.session:
        return redirect ("/")
    context={
        "username": User.objects.get(id= request.session['userid']),
        "postmess": Message.objects.all(),
        "postcomm": Comment.objects.all(),
    }
    return render(request, "wallapp/wall.html",context)

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
        return redirect("/wall")

def login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        request.session['userid'] = User.objects.get(email= request.POST['email']).id
        return redirect("/wall")

def logout(request):
    request.session.clear()
    return redirect("/")

def post(request):
    poster=User.objects.get(id=request.session['userid'])
    postmes= Message.objects.create(poster= poster, message= request.POST['message'])
    return redirect("/wall")

def comment(request):
    commenter= User.objects.get(id=request.session['userid'])
    postmes = Message.objects.get(id= request.POST['mid'])
    postcom= Comment.objects.create(commenter= commenter, messages= postmes , comment= request.POST['comment'])
    return redirect('/wall')

def messagedelete(request,x):
    messdel = Message.objects.get(id=x)
    messdel.delete()
    return redirect("/wall")

def commentdelete(request,y):
    commdel = Comment.objects.get(id=y)
    commdel.delete()
    return redirect("/wall")
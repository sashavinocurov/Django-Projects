from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
import bcrypt

from .models import User, Travel

def index(request):
    return render(request, "travelapp/login.html")

def register(request):
    errors= User.objects.user_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        encrypted = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        regester = User.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], email= request.POST['email'], password= encrypted)
        request.session['userid'] = User.objects.get(email= request.POST['email']).id
        return redirect("/dashboard")

def login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        request.session['userid'] = User.objects.get(email= request.POST['email']).id
        return redirect("/dashboard")
def logout(request):
    request.session.clear()
    return redirect("/")

def dashboard(request):
    if 'userid' not in request.session:
        return redirect ("/")
    context={
        "username": User.objects.get(id= request.session['userid']),
        "alltrips": Travel.objects.all().order_by("-created_at")
    }
    return render(request, "travelapp/dashboard.html",context)

def create(request):
    if 'userid' not in request.session:
        return redirect ("/")
    context={
        "username": User.objects.get(id=request.session['userid'])
    }
    return render(request, "travelapp/create.html",context)

def delete(request,x):
    if 'userid' not in request.session:
        return redirect ("/")
    travdel= Travel.objects.get(id=x)
    travdel.delete()
    return redirect('/dashboard')

def newtrip(request):
    errors = Travel.objects.travel_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create')
    travelers=User.objects.get(id=request.session["userid"])
    newtravel= Travel.objects.create(destination= request.POST['destination'], start_date= request.POST['start_date'], end_date= request.POST['end_date'], plan= request.POST['plan'], travelers=travelers)
    return redirect('/dashboard')

def edit(request, x):
    if 'userid' not in request.session:
        return redirect ("/")
    travelid= Travel.objects.get(id=x)
    context={
        "username": User.objects.get(id= request.session['userid']),
        "travelid": Travel.objects.get(id=x),
        "startdate": datetime.strftime(travelid.start_date, '%Y-%m-%d'),
        "enddate": datetime.strftime(travelid.end_date, '%Y-%m-%d'),
    }
    return render(request, "travelapp/edit.html", context)

def edittravel(request, x):
    if 'userid' not in request.session:
        return redirect ("/")
    errors = Travel.objects.travel_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{x}')
    else:
        travelid= Travel.objects.get(id=x)
        travelid.destination= request.POST['destination']
        travelid.start_date= request.POST['start_date']
        travelid.end_date= request.POST['end_date']
        travelid.plan= request.POST['plan']
        travelid.save()
        return redirect("/dashboard")
    
def info(request,x):
    if 'userid' not in request.session:
        return redirect ("/")
    Travel.objects.get(id=x)
    context={
        "username": User.objects.get(id= request.session['userid']),
        "trip": Travel.objects.get(id=x),
    }
    return render(request, "travelapp/info.html", context)



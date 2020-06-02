from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime

from .models import Tvshow

def show(request):
    context={
        "allshows": Tvshow.objects.all(),
    }
    return render(request, "tvshowapp/show.html", context)

def new(request):
    return render(request, "tvshowapp/newshow.html")

def createnew(request):
    errors = Tvshow.objects.newshow_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        Tvshow.objects.create(title= request.POST['title'], network= request.POST['network'], release_date= request.POST['release_date'], description= request.POST['description'])
        return redirect("/")

def showinfo(request,x):
    Tvshow.objects.get(id=x)
    context={
        "showid": Tvshow.objects.get(id=x)
    }
    return render(request, "tvshowapp/showinfo.html", context)

def edit(request,x):
    Tvshow.objects.get(id=x)
    showid= Tvshow.objects.get(id=x)
    context={
        "showid": Tvshow.objects.get(id=x),
        "daterel": datetime.strftime(showid.release_date, '%Y-%m-%d')
    }
    return render(request, "tvshowapp/editshow.html", context)

def editinfo(request,x):
    errors = Tvshow.objects.newshow_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{x}')
    showid= Tvshow.objects.get(id=x)
    showid.title= request.POST['title']
    showid.network= request.POST['network']
    showid.release_date= request.POST['release_date']
    showid.description= request.POST['description']
    showid.save()
    context={
    "showid": Tvshow.objects.get(id=x)
}
    return redirect(f"/{x}", context)

def delete(request,x):
    showdel= Tvshow.objects.get(id=x)
    showdel.delete()
    return redirect("/")
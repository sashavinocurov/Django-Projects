from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context ={
        "time": strftime("%m-%d-%Y", gmtime()),
        "time1": strftime("%H:%M %Z", gmtime())
    }
    return render(request, "time_app/index.html", context)

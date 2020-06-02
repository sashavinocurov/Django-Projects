from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    context = {
        'randomword': get_random_string(length=14),     
        "counter": request.session["counter"]
        }
    return render(request, "wordapp/index.html", context)

def generate(request):
    request.session["counter"] +=1
    return redirect("/")

def destroy(request):
    request.session["counter"] = 0
    return redirect ("/")
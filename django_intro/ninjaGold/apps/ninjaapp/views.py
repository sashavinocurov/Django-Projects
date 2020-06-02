from django.shortcuts import render, HttpResponse, redirect 
import random


def index(request):
    if "goldcounter" not in request.session:
        request.session["goldcounter"] = 0
    if "log" not in request.session:
        request.session["log"] = []
    context= {
        "goldcounter": request.session["goldcounter"],
        "log": request.session["log"]

    }
    return render(request, "ninjaapp/index.html", context)

def getgold(request):
    location = request.POST["location"]
    if location == "farmgold":
        goldcounter = random.randint(10,20)
    elif location == "cavegold":
        goldcounter = random.randint(5,10)
    elif location == "housegold":
        goldcounter = random.randint(2,5)
    else:
        goldcounter = random.randint(-50,50)

    if goldcounter > 0: 
        request.session["log"].insert(0, f"{goldcounter} Gold Earned from {location}")
    else: 
        request.session["log"].insert(0, f"{goldcounter} Gold Lost from {location}")
    request.session["goldcounter"] += goldcounter
    return redirect("/")

def reset(request):
    request.session.pop("goldcounter")
    request.session.pop("log")
    return redirect("/")
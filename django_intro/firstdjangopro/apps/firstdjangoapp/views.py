from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "name": "Sasha",
        "favorite_color": "orange",
        "pets": ["Barsik","Tuzik","Shmonya"]
    }
    return render(request, "firstdjangoapp/index.html", context)
    # return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect ("/")

def show(request, number):
    return HttpResponse("Placeholder to display blog number:{}".format(number))

def edit(request, number):
    return HttpResponse("Placeholder to edit blog {}".format(number))

def destroy(request, number):
    return redirect ("/")
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def new(request):
    return HttpResponse("New page from the first app")

def one_method(request):
    pass
    
def another_method(request, my_val):
    pass
    
def yet_another(request, name):
    pass
    
def one_more(request, id, color):
    pass
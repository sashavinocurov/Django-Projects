from django.shortcuts import render, redirect 
from .models import Comment
from .forms import CommentForm
import urllib.request , json

def index(request):
    comments = Comment.objects.order_by('-created_at')

    context={
        'comments' : comments
    }

    return render(request, 'guestbook/guestbook.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect ('index')
    
    else:
        form = CommentForm()

    context = {
        'form' : form
    }

    return render(request, 'guestbook/sign.html', context)


def search (request):
    url = 'http://img.omdbapi.com/?apikey=b923f853&' +str(request.POST['title'])
    response= urllib.request.urlopen(url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)
    request.session['movietitle'] = data['title']


    return redirect('/movie')

def movies (request):
    if 'movietitle' not in request.session:
        request.session['movietitle'] = ''
    context={
        'movie': request.session['movietitle']
    }

    return render(request, 'guestbook/movie.html', context)
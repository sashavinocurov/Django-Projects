from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^messdel/(?P<x>\d+)$', views.messagedelete),
    url(r'^comdel/(?P<y>\d+)$', views.commentdelete),
    url(r'^register$', views.regester),
    url(r'^comment$', views.comment),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^post$', views.post),
    url(r'^wall$', views.wall),
    url(r'^$', views.index),
]
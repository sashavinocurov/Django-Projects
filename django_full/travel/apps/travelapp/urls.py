from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
    url(r'^newtrip$', views.newtrip),
    url(r'^register$',views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^info/(?P<x>\d+)$', views.info),
    url(r'^edit/(?P<x>\d+)$', views.edit),
    url(r'^delete/(?P<x>\d+)$', views.delete),
    url(r'^edittravel/(?P<x>\d+)$', views.edittravel),
]
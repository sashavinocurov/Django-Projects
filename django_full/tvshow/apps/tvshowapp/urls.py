from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^editinfo/(?P<x>\d+)$', views.editinfo),
    url(r'^delete/(?P<x>\d+)$', views.delete),
    url(r'^edit/(?P<x>\d+)$', views.edit),
    url(r'^(?P<x>\d+)$', views.showinfo),
    url(r'^createnew$', views.createnew),
    url(r'^new$', views.new),
    url(r'^$', views.show),
    
]
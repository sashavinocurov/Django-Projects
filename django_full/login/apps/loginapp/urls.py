from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register$', views.regester),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^$', views.index),
]
from django.conf.urls import url
from.import views


urlpatterns=[
    url(r'^(?P<number>\d+)/delete$', views.destroy),
    url(r'^(?P<number>\d+)/\w+$', views.edit),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'^$', views.index),
]

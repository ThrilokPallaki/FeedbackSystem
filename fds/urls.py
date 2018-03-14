from django.conf.urls import url
from . import views

app_name='fds'
urlpatterns= [
    url(r'^$', views.fdsHome, name='fdsHome'),
    url(r'^rank/$', views.ranking, name='ranking'),
    url(r'^rank/(?P<rank_id>[0-9]+)/$', views.questions, name='questions'),
    url(r'^goobye/$', views.goodBye, name='goodbye'),
    url(r'^ratingchart/$', views.ratingGraph, name='ratingchart'),
]

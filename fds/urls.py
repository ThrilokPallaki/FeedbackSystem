from django.conf.urls import url
from . import views

app_name='fds'
urlpatterns= [
    # url(r'^$', views.fdsHome, name='fdsHome'),
    #url(r'^rank/$', views.ranking, name='ranking'),
    #url(r'^$', views.fdsuser, name="fds"),
    #url(r'^goobye/$', views.goodBye, name='goodbye'),
    url(r'^$', views.UserCreateView.as_view(), name='createUser'),
    url(r'thankyou/(?P<user>[0-9]+)/$', views.ThankingYouView.as_view(), name='thankyou'),
    url(r'^rank/(?P<user_id>[0-9]+)/$', views.questions, name='questions'),
    url(r'goodbye/$', views.GoodByeView.as_view(), name='goodbye'),
    url(r'^ratingchart/$', views.RatingGraphView.as_view(), name='ratingchart'),
]

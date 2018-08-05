from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^POST/$', views.CommentRequest.as_view(), name = 'CommentRequest'),
    url(r'^socialauth/$', views.socialauth.as_view(), name='socialauth'),
]

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login.html/$', views.login, name='login'),
    re_path(r'^logout.html/$', views.logout_user, name='logout'),
    re_path(r'^start.html/$', views.start, name='start'),
]
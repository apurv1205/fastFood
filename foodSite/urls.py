from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', auth_views.login,name="login"),
    url(r'^logout/$', views.logout_page,name="logout_page"),
    url(r'^accounts/login/$', auth_views.login,name="login"), # If user is not login it will redirect to login page
    url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$', views.register_success,name="register_success"),
    url(r'^home/$', views.home,name="home"),
]
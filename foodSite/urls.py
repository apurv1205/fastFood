from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 	url(r'^$', views.main_page,name="main_page"),
	url(r'^user/(\w+)/$', views.user_page,name="user_page"),
	url(r'^login/$', auth_views.login,name="login"),
	url(r'^logout/$', views.logout_page,name="logout_page"),
	url(r'^register/$', views.register_page,name="register_page"),
	]
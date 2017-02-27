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
    url(r'^register/home/$', views.home,name="home"),
    url(r'^home/$', views.home,name="home"),
    url(r'^rest/(?P<pk>\d+)/$', views.rest_detail, name='rest_detail'),
    url(r'^change_status/(?P<pk>\d+)/$', views.change_status, name='change_status'),
    url(r'^item/(?P<pk>\d+)/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name = 'checkout'),
    url(r'^order_history/$', views.order_history, name = 'order_history'),
    url(r'^order_history_user/$', views.order_history_user, name = 'order_history_user'),
    url(r'^current_orders/$', views.current_orders, name='current_orders'),
    url(r'^cancel_order/(?P<pk>\d+)/$', views.cancel_order, name='cancel_order'),
    url(r'^inc_count/(?P<pk>\d+)/$', views.inc_count, name = 'inc_count'),
    url(r'^dec_count/(?P<pk>\d+)/$', views.dec_count, name = 'dec_count')
]
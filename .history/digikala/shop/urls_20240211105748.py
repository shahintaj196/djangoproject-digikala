
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld, name='home'),
    path('about/',views.about, name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path
]

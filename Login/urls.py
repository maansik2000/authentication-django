from django.contrib import admin
from django.urls import path, include
from Login.views import register, loginPage,home,logoutUser

urlpatterns = [
    path('',home,name="home"),
    path('login/',loginPage,name="login"),
    path('register/',register,name="register"),
    path('logout/',logoutUser,name="logout"),
]

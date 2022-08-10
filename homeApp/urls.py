from django.contrib import admin
from django.urls import path
from homeApp import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('register',views.registerNewUser,name="register"),
    path('test',views.test,name="test"),
    path('profile',views.profile,name="profile"),
    path('deposite',views.depositeMoney,name="deposite"),
    path('withdraw',views.withdrawMoney,name="withdraw")
]
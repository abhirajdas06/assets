from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('profile/', views.profile, name="Profile")
]
from django.contrib import admin
from django.urls import path
from .views import index
from .views import login

urlpatterns = [
    path("",index),
    path("login/",login),
    path("admin/",admin.site.urls)
]
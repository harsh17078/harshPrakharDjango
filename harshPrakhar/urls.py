from django.contrib import admin
from django.urls import path
from .views import index
from .views import login
from .views import signup
urlpatterns = [
    path("",index),
    path("login/",login),
    path("signup/",signup),
    path("admin/",admin.site.urls)

]
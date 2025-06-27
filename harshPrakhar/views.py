from django.shortcuts import render
def index(req):
    return render(req,"home.html")
def login(req):
    return render(req,"login.html")
def signup(req):
    return render(req,"signUp.html")
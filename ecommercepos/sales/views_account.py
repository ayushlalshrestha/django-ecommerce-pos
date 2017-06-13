from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Sale, Product, Customer

def login_page(request):
    return render(request, "sales/login_page.html", { })


def login_process(request):
    if request.method == 'POST':
        username = request.POST.get("username")    
        password = request.POST.get("password")
        user = auth.authenticate(username = username, password = password)
        auth.login(request, user)
        if user is not None:
            print(username +  str(password))
            print(user.first_name + " - - - - - - - - - - - ------------------------------")

            return HttpResponse("DONE !!")
        else:
            print("Not Done !!")      
            return HttpResponse("Wrong User Credentials !!")

def logout(request):
    if request.user:
        auth.logout(request)
    return HttpResponseRedirect("/sales")

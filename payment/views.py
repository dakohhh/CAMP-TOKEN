from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.



def add_money(request:HttpRequest):
    return render(request, "")
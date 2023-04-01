


from django.http import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from main.forms import PayMerchantForm
from django.contrib.auth.decorators import login_required



@login_required(login_url="login")
def pay(request:HttpRequest):

    form = PayMerchantForm()


    context = {"form": form}

    return render(request, "pay.html", context)









def confirm_merchant_id(request:HttpRequest):


    return JsonResponse({"yeah"})
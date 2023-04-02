from django.http import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from main.forms import PayMerchantForm
from django.contrib.auth.decorators import login_required

from main.utils.repsonse import customResponse, CustomResponse



@login_required(login_url="login")
def pay(request:HttpRequest):

    form = PayMerchantForm()


    context = {"form": form}

    return render(request, "pay.html", context)









def confirm_merchant_id(request:HttpRequest):

    merchant_id = request.GET.get("id")


    return CustomResponse(200, f"yeah it works ,id = {merchant_id}")
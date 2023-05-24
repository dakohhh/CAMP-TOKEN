from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from utils.shortcuts import redirect_not_merchant, redirect_not_student
from user.models import User
from utils.crud import fetchone
from utils.response import CustomResponse, NotFoundResponse
# Create your views here.

@login_required(login_url="login")
@redirect_not_student
def pay_merchant(request:HttpRequest):


    context = {"user": request.user}

    return render(request, "transactions/pay_merchants.html", context)



def refund_student(request:HttpRequest):
    

    return render(request, "transactions/refund_student.html")



def confirm_merchant_wallet(request:HttpRequest):

    merchant_wallet_id = request.GET.get("id")

    user = fetchone(User, wallet_id=merchant_wallet_id)

    if not user or not user.is_merchant :
        return NotFoundResponse("INCORRECT MERCHANT")
    
    
    return CustomResponse("Merchant Get Successfully", data=user.business_name)

# 4798422654



    
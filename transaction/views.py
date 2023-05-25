from django.shortcuts import render
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from utils.generate import generate_transaction_id
from utils.shortcuts import redirect_not_merchant, redirect_not_student
from user.models import User
from utils.crud import fetchone
from utils.response import CustomResponse, NotFoundResponse, BadRequest
# Create your views here.

@login_required(login_url="login")
@redirect_not_student
def pay_merchant(request:HttpRequest):

    if request.method == "POST":

        merchant_wallet_id = int(request.POST.get("merchant_wallet_id"))

        amount = float(request.POST.get("amount"))

        trasaction_pin = int(request.POST.get("trans_pin"))

        test_pin = 5050

        if len(str(merchant_wallet_id)) != 10 or len(str(trasaction_pin)) != 4:
            return BadRequest("Validation Error: check Wallet ID (must be 10-digits) or Transaction Pin(must be 4-digits)")
        
        if trasaction_pin != test_pin:
            return BadRequest("Incorrect Pin")
        
        if request.user.balance < amount:

            return BadRequest("Insufficient Balance, you may need to fund your wallet")
        
        merchant = fetchone(User, wallet_id=merchant_wallet_id)

        trasaction_id = generate_transaction_id(15)

        if merchant is None:
            return NotFoundResponse("Merchant ID Not Found")
        
        return CustomResponse(msg="Things Worked Out", data=merchant)

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



    
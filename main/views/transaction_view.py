from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from main.forms import PayMerchantForm
from main.models import CustomUser
from main.utils.shortcuts import get_object_or_none
from main.utils.repsonse import(CustomResponse, HttpResponseNotFound, HttpResponseUnauthorized,
                                 HttpResponsePaymentRequired,HttpResponseBadRequest)



@login_required(login_url="login")
@transaction.atomic
def pay_merchant(request:HttpRequest):

    form = PayMerchantForm()

    if request.method == "POST":

        test_pin = 5050
        
        merchant_wallet_id = request.POST.get("merchant_wallet_id")

        amount = request.POST.get("amount")
        
        trans_pin = request.POST.get("trans_pin")

        # payment to merchant

        if int(trans_pin) != test_pin:
            return HttpResponseUnauthorized("Incorrect Pin")


        if request.user.balance < float(amount):
            return HttpResponsePaymentRequired("Insufficient Balance, you may need to fund your wallet")
        
        merchant = get_object_or_none(CustomUser, wallet_id=merchant_wallet_id)
        
        try:

            with transaction.atomic():
                request.user.balance -= float(amount)

                request.user.save()

                merchant.balance += float(amount)

                merchant.save()
        except ValidationError:
            return HttpResponseBadRequest("wisdomda")

        print(merchant.email, merchant.balance)

        return redirect("payment_success")

    context = {"form": form}

    return render(request, "transactions/pay_merchant.html", context)



@login_required(login_url="login")
def payment_success(request:HttpRequest):

    return render(request, "transactions/pay_success.html")



@login_required(login_url="login")
def payment_success(request:HttpRequest):

    return render(request, "transactions/pay_success.html")



@login_required(login_url="login")
def confirm_merchant_wallet_id(request:HttpRequest):

    try:
        merchant_id = request.GET.get("id")

        merchant = CustomUser.objects.get(wallet_id=merchant_id)

        # 4318883660

        print(merchant.business_name)
    except:
        return HttpResponseNotFound("Merchant Wallet ID not Found")
    
    if not merchant.is_merchant:
        return HttpResponseNotFound("Merchant Wallet ID not Found")


    return CustomResponse("ID Confirmed Successfully", data=merchant.business_name)
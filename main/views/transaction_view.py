from django.http import HttpRequest
from django.shortcuts import redirect, render
from main.forms import PayMerchantForm
from django.contrib.auth.decorators import login_required
from main.utils.repsonse import CustomResponse, HttpResponseNotFound, HttpResponseUnauthorized
from main.models import CustomUser



@login_required(login_url="login")
def pay_merchant(request:HttpRequest):

    form = PayMerchantForm()

    if request.method == "POST":

        test_pin = 5050
        
        merchant_wallet_id = request.POST.get("merchant_wallet_id")

        amount = request.POST.get("amount")
        
        trans_pin = request.POST.get("trans_pin")

        csrf_token = request.POST.get("csrfmiddlewaretoken")

        print(merchant_wallet_id, amount ,trans_pin, csrf_token)


        if int(trans_pin) != test_pin:
            return HttpResponseUnauthorized("Incorrect Pin")
        
        else:
            return redirect("payment_success")

    context = {"form": form}

    return render(request, "transactions/pay_merchant.html", context)



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
        return HttpResponseNotFound("Wallet ID not Found")


    return CustomResponse("ID Confirmed Successfully", data=merchant.business_name)
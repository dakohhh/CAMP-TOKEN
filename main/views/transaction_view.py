from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render
from main.forms import PayMerchantForm
from django.contrib.auth.decorators import login_required
from main.utils.repsonse import CustomResponse
from main.models import CustomUser



@login_required(login_url="login")
def pay(request:HttpRequest):

    form = PayMerchantForm()


    context = {"form": form}

    return render(request, "pay.html", context)









def confirm_merchant_wallet_id(request:HttpRequest):

    try:
        merchant_id = request.GET.get("id")

        merchant = CustomUser.objects.get(wallet_id=merchant_id)

        # 4318883660

        print(merchant.business_name)
    except:
        return CustomResponse(HttpResponseNotFound.status_code, "Wallet ID not Found", False)


    return CustomResponse(200, "ID Confirmed Successfully", data=merchant.business_name)
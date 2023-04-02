from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render
from main.forms import PayMerchantForm
from django.contrib.auth.decorators import login_required
from main.utils.repsonse import CustomResponse
from main.models import CustomUser



@login_required(login_url="login")
def pay_merchant(request:HttpRequest):

    form = PayMerchantForm()

    if request.method == "POST":
        merchant_wallet_id = request.POST.get("merchant_wallet_id")

        amount = request.POST.get("amount")

        print(merchant_wallet_id, amount)

    context = {"form": form}

    return render(request, "transactions/pay_merchant.html", context)


@login_required(login_url="login")
def confirm_pay_merchant(request:HttpRequest):
    pass






@login_required(login_url="login")
def confirm_merchant_wallet_id(request:HttpRequest):

    try:
        merchant_id = request.GET.get("id")

        merchant = CustomUser.objects.get(wallet_id=merchant_id)

        # 4318883660

        print(merchant.business_name)
    except:
        return CustomResponse(HttpResponseNotFound.status_code, "Wallet ID not Found", False)


    return CustomResponse(200, "ID Confirmed Successfully", data=merchant.business_name)
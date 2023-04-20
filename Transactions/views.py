from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.db import transaction
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from main.forms import PayMerchantForm
from main.models import CustomUser
from .models import Transactions
from utils.shortcuts import forbidden_if_already_refunded, generate_transaction_id, get_object_or_none, forbidden_if_merchant, forbidden_if_student
from utils.crud import pay_merchant_transaction, refund_student_transaction
from utils.repsonse import(CustomResponse, HttpResponseNotFound, HttpResponseUnauthorized,HttpResponseBadRequest)



@login_required(login_url="login")
@forbidden_if_merchant
@transaction.atomic
def pay_merchant(request:HttpRequest):

    form = PayMerchantForm()

    if request.method == "POST":

        test_pin = 5050
        
        merchant_wallet_id = request.POST.get("merchant_wallet_id")

        amount = float(request.POST.get("amount"))
        
        trans_pin = int(request.POST.get("trans_pin"))

        if trans_pin != test_pin:
            return HttpResponseUnauthorized("Incorrect Pin")
        
        elif request.user.balance < amount:

            return HttpResponseBadRequest("Insufficient Balance, you may need to fund your wallet")
        
        else:
            merchant = get_object_or_none(CustomUser, wallet_id=merchant_wallet_id)

            transaction_id = generate_transaction_id(15)


            if merchant is None:
                return HttpResponseNotFound("Merchant not found")


            pay_merchant_transaction(request, merchant, amount, transaction_id)

            return redirect("payment_merchant_status",transaction_id=transaction_id)


    context = {"form": form}

    return render(request, "transactions/pay_merchant.html", context)



@login_required(login_url="login")
@forbidden_if_student
@forbidden_if_already_refunded
@transaction.atomic
def refund_student(request:HttpRequest, transaction_id:str):

    _transaction = get_object_or_none(Transactions, transaction_id=transaction_id)

    if not _transaction:
        # ??? return custom 404 page
        raise Http404()
    
    if request.method == "POST":
        test_pin = 5050

        trans_pin = int(request.POST.get("trans_pin"))

        if trans_pin != test_pin:
            return HttpResponseUnauthorized("Incorrect Pin")

        elif request.user.balance < float(_transaction.amount):

            return HttpResponseBadRequest("Insufficient Balance, you may need to fund your wallet")
        
        
        refund_transaction_id = generate_transaction_id(15)

        refund_student_transaction(request, _transaction, refund_transaction_id)

        return redirect("refund_student_status", transaction_id=transaction_id)
            

    context = {"transaction":_transaction}

    return render(request, "transactions/refund_student.html", context)




@login_required(login_url="login")
@forbidden_if_merchant
def payment_merchant_status(request:HttpRequest, transaction_id):

    transaction = get_object_or_none(Transactions, transaction_id=transaction_id)

    if not transaction:

        # raise Http404 here
    
        return HttpResponse("Page not found", status=404)
    


    context = {"transaction": transaction}

    return render(request, "transactions/pay_merchant_status.html", context)



@login_required(login_url="login")
@forbidden_if_student
def refund_student_status(request:HttpRequest, transaction_id):

    transaction = get_object_or_none(Transactions, transaction_id=transaction_id)

    if not transaction:

        # raise Http404 here

        return HttpResponse("Page not found", status=404)
    

    context = {"transaction": transaction}

    return render(request, "transactions/refund_student_status.html", context)



@login_required(login_url="login")
def confirm_merchant_wallet_id(request:HttpRequest):

    merchant_wallet_id = request.GET.get("id")


    merchant = get_object_or_none(CustomUser,wallet_id=merchant_wallet_id)

    # 4558664727
    
    if not merchant or (merchant.is_merchant == False):
        return HttpResponseNotFound("Merchant Wallet ID not Found")

    return CustomResponse("ID Confirmed Successfully", data=merchant.business_name)





@login_required(login_url="login")
@forbidden_if_merchant
def fund_student_wallet(request:HttpRequest):

    
    context = {"balance": request.user.balance}
    
    return render(request, "transactions/fund_student_wallet.html", context)

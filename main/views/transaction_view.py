from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from main.forms import PayMerchantForm
from main.models import CustomUser, Transactions
from main.utils.shortcuts import generate_transaction_id, get_object_or_none, does_object_exists
from main.utils.repsonse import(CustomResponse, HttpResponseNotFound, HttpResponseUnauthorized,HttpResponseBadRequest)



@login_required(login_url="login")
@transaction.atomic
def pay_merchant(request:HttpRequest):

    form = PayMerchantForm()

    if request.method == "POST":

        test_pin = 5050
        
        merchant_wallet_id = request.POST.get("merchant_wallet_id")

        amount = float(request.POST.get("amount"))
        
        trans_pin = request.POST.get("trans_pin")


        if int(trans_pin) != test_pin:
            return HttpResponseUnauthorized("Incorrect Pin")

        elif request.user.balance < amount:

            return HttpResponseBadRequest("Insufficient Balance, you may need to fund your wallet")
        
        else:

            # Get the merchant from the wallet id
            
            merchant = get_object_or_none(CustomUser, wallet_id=merchant_wallet_id)

            transaction_id = generate_transaction_id(15)


            # - START TRANSACTION LOOP

            try:
                with transaction.atomic():
                
                    request.user.balance -= amount

                    request.user.save()

                    merchant.balance += amount

                    merchant.save()

                    Transactions.objects.create(transaction_id=transaction_id, sender=request.user, recipient=merchant, amount=amount, status=1)

            except ValidationError:

                Transactions.objects.create(transaction_id=transaction_id, sender=request.user, recipient=merchant, amount=amount, status=0)

                return HttpResponseBadRequest("Transaction Failed")

    
            return redirect("payment_merchant_success",transaction_id=transaction_id)

    context = {"form": form}

    return render(request, "transactions/pay_merchant.html", context)



@login_required(login_url="login")
def payment_success(request:HttpRequest, transaction_id):

    transaction = get_object_or_none(Transactions, transaction_id=transaction_id)

    if not transaction:
        return Exception
    
    recipient = transaction.recipient.business_name

    amount = transaction.amount

    date_added = transaction.date_added

    transaction = {
        "recipient": recipient, 
        "amount": amount,

        "date_added": date_added

    }

    context = {"transaction": transaction}

    return render(request, "transactions/pay_success.html", context)



@login_required(login_url="login")
def payment_failed(request:HttpRequest):

    return render(request, "transactions/pay_failed.html")



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
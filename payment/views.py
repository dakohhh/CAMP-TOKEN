import hashlib
import hmac
import os
from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from transaction.models import Transactions
from utils.generate import generate_transaction_id
from utils.crud import add_money_transaction
from utils.request import add_money_request, PaystackAPIException
from utils.response import CustomResponse, ServiceUnavailable
from utils.shortcuts import redirect_not_student
from utils.exceptions import TransactionFailed
from dotenv import load_dotenv

load_dotenv()

# Create your views here.


@login_required
@redirect_not_student
def add_money(request:HttpRequest):

    if request.method == "POST":

        email = request.user.email

        amount = int(request.POST.get("amount"))

        transaction_id = generate_transaction_id(15)

        try:

            checkout = add_money_request(request, email, amount, transaction_id)

            new_transaction = Transactions(transaction_id=transaction_id, student=request.user, amount=amount, transaction_type=Transactions.PAID_ONLINE, transaction_status=Transactions.PENDING)
            
            return CustomResponse("Payment Link Generated Successfull", data={"checkout": checkout})

        except PaystackAPIException:
            
            return ServiceUnavailable("Something went wrong, please try again")

    return render(request, "addmoney/add_money.html")



@csrf_exempt
def webhook(request:HttpRequest):

    if request.method == "POST":
        try:

            secret = str(os.getenv("PAYSTACK_SECRET_KEY"))

            signature = request.headers.get('x-paystack-signature')

            hash_signature = hmac.new(secret.encode('utf-8'), request.body, hashlib.sha512).hexdigest()

            if signature != hash_signature:
                return HttpResponse(status=403)
            
            
            request_data = dict(request.body.decode("utf-8")).data

            add_money_transaction(request, request_data.reference, int(request_data.amount), request_data.status)

            return HttpResponse(status=200)
        
        except TransactionFailed:

            return HttpResponse(status=500)


    return CustomResponse("Get Wekks")

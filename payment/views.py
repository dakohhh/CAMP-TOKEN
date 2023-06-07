import hashlib
import hmac
import os
import json
from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from transaction.models import Transactions
from user.models import User
from utils.generate import generate_transaction_id
from utils.crud import add_money_transaction, fetchone
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
            
            
            request_data = json.loads(request.body).get("data")

            user_reference = request_data.get("customer")

            user = fetchone(User, email=user_reference.get("email"))


            add_money_transaction(user, request_data.get("reference"), float(request_data.get("amount") / 100), request_data.get("status"))

            return HttpResponse(status=200)
        
        except TransactionFailed:

            return HttpResponse(status=500)


    return CustomResponse("Get Wekks")

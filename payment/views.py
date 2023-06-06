from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from transaction.models import Transactions
from utils.generate import generate_transaction_id
from utils.request import add_money_transaction, PaystackAPIException
from utils.response import CustomResponse, ServiceUnavailable
from utils.shortcuts import redirect_not_student

# Create your views here.


@login_required
@redirect_not_student
def add_money(request:HttpRequest):

    if request.method == "POST":

        email = request.user.email

        amount = int(request.POST.get("amount"))

        transaction_id = generate_transaction_id(15)

        try:

            checkout = add_money_transaction(request, email, amount, transaction_id)

            new_transaction = Transactions(transaction_id=transaction_id, student=request.user, amount=amount, transaction_type=Transactions.PAID_ONLINE, transaction_status=Transactions.PENDING)

            print(checkout)


        except PaystackAPIException as e:
            
            return ServiceUnavailable(e)

    return render(request, "addmoney/add_money.html")


def add_money_success(request:HttpRequest):


    return HttpResponse("Payment Success boi")
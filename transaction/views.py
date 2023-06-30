from django.http import Http404
from django.shortcuts import render
from django.http.request import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from transaction.models import Transactions
from utils.generate import generate_transaction_id
from utils.order import group_transaction_by_date
from utils.shortcuts import redirect_not_merchant, redirect_not_student
from user.models import User
from utils.crud import fetchone, pay_merchant_transaction, refund_student_transaction
from utils.response import CustomResponse, NotFoundResponse, BadRequest, ServiceUnavailable
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
            return BadRequest("Validation Error: check Wallet ID (must be 10-digits) or Transaction Pin(must be 4-digits)", data="00")
        
        if trasaction_pin != test_pin:
            return BadRequest("Incorrect Pin", data="01")
        
        if request.user.balance < amount:

            return BadRequest("Insufficient Balance", data="01")
        
        merchant = fetchone(User, wallet_id=merchant_wallet_id)

        transaction_id = generate_transaction_id(15)

        if merchant is None:
            return NotFoundResponse("Merchant ID Not Found", data="00")

        payment = pay_merchant_transaction(request, merchant, amount, transaction_id)

        if payment.transaction_status == 0:
            return ServiceUnavailable(msg="Something went wrong, please try again", data=payment.to_dict())
        
        return CustomResponse(msg="Your transfer is on the way!", data=payment.to_dict())


    context = {"user": request.user}

    return render(request, "transactions/pay_merchants.html", context)



@login_required(login_url="login")
@redirect_not_merchant
def refund_student(request:HttpRequest, transaction_id):

    transaction = fetchone(Transactions, transaction_id=transaction_id)

    if transaction == None or transaction.recipient != request.user:
        return render(request, "404.html", status=404)
    

    if request.method == "POST":

        trasaction_pin = int(request.POST.get("trans_pin"))

        test_pin = 5050

        if trasaction_pin != test_pin:
            return BadRequest("Incorrect Pin", data="01")
        
        if request.user.balance < transaction.amount:

            return BadRequest("Insufficient Balance", data="01")


        transaction_id = generate_transaction_id(15)

        refund = refund_student_transaction(request, transaction, transaction_id)

        if refund.transaction_status == 0:
            return ServiceUnavailable(msg="Something went wrong, please try again", data=refund.to_dict())
        
        return CustomResponse(msg="Refund is on the way!", data=refund.to_dict())


    context = {"user": request.user, "transaction":transaction}
    
    return render(request, "transactions/refund_student.html", context)





@login_required(login_url="login")
def get_student_transactions(request:HttpRequest):

    if request.user.is_merchant:
        trans_history = Transactions.objects.filter(merchant=request.user).order_by("-date_added").exclude(transaction_status=Transactions.FAILED, initiated_by_student=True)
    else:
        trans_history = Transactions.objects.filter(student=request.user).order_by("-date_added").exclude(transaction_status=Transactions.FAILED, initiated_by_student=False)

    
    page_number = request.GET.get('page') 
    per_page = 6


    paginator = Paginator(trans_history, per_page)

    try:
 
        page_transactions = paginator.page(int(page_number))


        page_detials = {
            'has_previous': page_transactions.has_previous(),
            'has_next': page_transactions.has_next(),
            'total_pages': paginator.num_pages
        }

        trans_history = group_transaction_by_date(page_transactions.object_list)

        return CustomResponse("Get Transactions Succussfull", data=trans_history, page_detials=page_detials)
    
    
    except PageNotAnInteger:
        return BadRequest("Invalid page number")
    
    except EmptyPage:
        return NotFoundResponse("Page out of range")


def confirm_merchant_wallet(request:HttpRequest):

    merchant_wallet_id = request.GET.get("id")

    user = fetchone(User, wallet_id=merchant_wallet_id)

    if not user or not user.is_merchant :
        return NotFoundResponse("INCORRECT MERCHANT")
    
    
    return CustomResponse("Merchant Get Successfully", data=user.business_name)

# 4798422654



    
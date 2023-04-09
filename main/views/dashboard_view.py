
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from main.models import CustomUser, Transactions
from main.utils.shortcuts import group_transactions_by_date




@login_required(login_url="login")
def dashboard_student(request:HttpRequest):
    
    user = CustomUser.objects.get(email=request.user)

    if not user.is_student:
        return redirect("dashboard_merchant")
    

    trans_history = Transactions.objects.filter(sender=request.user).order_by("-date_added")

    transactions_by_date = group_transactions_by_date(trans_history)


    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "balance": user.balance,
        "wallet_id":user.wallet_id,
        "transactions_by_date": transactions_by_date
    }

    return render(request, "dashboard/dashboard_student.html", context)



@login_required(login_url="login")
def transactions_student(request):



    return render(request, "transaction/transaction_student.html")







@login_required(login_url="login")
def dashboard_merchant(request:HttpRequest):

    user = CustomUser.objects.get(email=request.user)

    if not user.is_merchant:
        return redirect("dashboard_student")

    trans_history = Transactions.objects.filter(recipient=request.user).order_by("-date_added")


    transactions_by_date = group_transactions_by_date(trans_history)

    context = {
        "business_name": user.business_name,
        "last_name": user.last_name,
        "balance": user.balance,
        "wallet_id":user.wallet_id, 
        "transactions_by_date": transactions_by_date
    }

    return render(request, "dashboard/dashboard_merchants.html", context)
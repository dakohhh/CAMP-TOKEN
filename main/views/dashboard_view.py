
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from main.models import CustomUser, Transactions




@login_required(login_url="login")
def dashboard_student(request:HttpRequest):
    
    user = CustomUser.objects.get(email=request.user)

    if not user.is_student:
        return redirect("dashboard_merchant")
    
    trans_history = Transactions.objects.filter(sender=request.user)


    for i in trans_history:
        print(i.recipient)
        print(i.status)
        print(i.date_added)
        print(i.amount)


    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "balance": user.balance,
        "wallet_id":user.wallet_id,
        "trans_history": trans_history 
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

    trans_history = Transactions.objects.filter(recipient=request.user)

    for i in trans_history:
        print(i.recipient)
        print(i.status)
        print(i.date_added)
        print(i.amount)
    
    context = {
        "business_name": user.business_name,
        "last_name": user.last_name,
        "balance": user.balance,
        "wallet_id":user.wallet_id, 
        "trans_history": trans_history
    }

    return render(request, "dashboard/dashboard_merchants.html", context)
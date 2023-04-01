
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from main.models import CustomUser




@login_required(login_url="login")
def dashboard_student(request:HttpRequest):
    
    user = CustomUser.objects.get(email=request.user)

    if not user.is_student:
        return redirect("dashboard_merchant")

    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "balance": user.balance,
        "wallet_id":user.wallet_id, 
        }

    return render(request, "dashboard/dashboard_student.html", context)






@login_required(login_url="login")
def dashboard_merchant(request:HttpRequest):

    user = CustomUser.objects.get(email=request.user)

    if not user.is_merchant:
        return redirect("dashboard_student")
    
    context = {
        "business_name": user.business_name,
        "last_name": user.last_name,
        "balance": user.balance,
        "wallet_id":user.wallet_id, 
    }

    return render(request, "dashboard/dashboard_merchants.html", context)
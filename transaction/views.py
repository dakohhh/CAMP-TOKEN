from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from utils.shortcuts import redirect_not_merchant, redirect_not_student

# Create your views here.

@login_required(login_url="login")
@redirect_not_student
def pay_merchant(request:HttpRequest):
    

    return render(request, "transactions/pay_merchants.html")





def refund_student(request:HttpRequest):
    

    return render(request, "transactions/refund_student.html")
    
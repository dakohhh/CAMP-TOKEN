from django.http.request import HttpRequest
from django.shortcuts import redirect
from main.utils.shortcuts import forbidden_if_merchant
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction





# This is just here inplace of the webhook API, would be implemented when live
@transaction.atomic
@forbidden_if_merchant
def fund_student_wallet_(request:HttpRequest):

    if request.method == 'POST':

        amount = request.GET.get('amount')

        with transaction.atomic():
            request.user.balance += amount

            request.user.save()

        return redirect("dashboard")



@csrf_exempt
def webhook(request:HttpRequest):

    pass

    
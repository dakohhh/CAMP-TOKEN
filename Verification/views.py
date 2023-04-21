import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from main.models import CustomUser
from utils.generate import generate_verification_token
from utils.repsonse import HttpResponseNotFound
from utils.shortcuts import get_verification_url, is_valid_verification
from utils.crud import delete_verfication_token, save_verifcation_token, update_user




def verify(request:HttpRequest):

    email = request.GET.get('email')
    token = request.GET.get('token')

    if not is_valid_verification(email, token):
        return HttpResponse("Invalid Token or Token is expired", status=400)

    if request.method == "POST":

        transaction_pin = request.POST.get("trans_pin")
        

        delete_verfication_token(token)
        update_user(email, transaction_pin)

        return HttpResponse("Account Vertified Successfully")
   

    return render(request, "verification/verification_page.html")



def resend_verification(request:HttpRequest):
    
    if request.method == "POST":

        email = request.POST.get("email")

        if CustomUser.objects.filter(email=email).exists():

            verification_token = generate_verification_token()

            expiration_time = timezone.now() + datetime.timedelta(minutes=30)

            save_verifcation_token(email, verification_token, expiration_time)


            verification_url = get_verification_url(request, email, verification_token)

            print(verification_url)
            
            # send welcome mail
        else:
            return HttpResponseNotFound("Email not found")

    return render(request,)







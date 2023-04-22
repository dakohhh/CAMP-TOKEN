import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from Verification.models import VerificationToken
from main.models import CustomUser
from utils.generate import generate_verification_token
from utils.repsonse import CustomResponse, HttpResponseNotFound, HttpResponseBadRequest
from utils.shortcuts import get_object_or_none, get_verification_url, is_valid_verification
from utils.crud import delete_verfication_token, save_verifcation_token, update_verication_token, update_user




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

        user = get_object_or_none(CustomUser, email=email)


        if user is not None and not user.is_verified:
            verification_token = generate_verification_token()

            expiration_time = timezone.now() + datetime.timedelta(minutes=30)

            if VerificationToken.objects.filter(user_email=email).exists():

                update_verication_token(email, verification_token, expiration_time)
            
            else:
                save_verifcation_token(email, verification_token, expiration_time)

            verification_url = get_verification_url(request, email, verification_token)

            print(verification_url)

            # send welcome mail
            return CustomResponse("Verification Link has been sent")

        elif user is not None and user.is_verified:
            
            return HttpResponseBadRequest("Email Already Verified")
        
        else:
            return HttpResponseNotFound("Email not found")

    return render(request,"verification/resend_verification_page.html")







from django.http import HttpRequest, HttpResponse
from main.utils.shortcuts import is_valid_verification
from main.utils.crud import delete_verfication_token, update_user_verication




def verify(request:HttpRequest):

    email = request.GET.get('email')
    token = request.GET.get('token')

    if is_valid_verification(email, token):

        delete_verfication_token(token)
        update_user_verication(email)

        return HttpResponse("Account Vertified Successfully")

    
    return HttpResponse("Invalid Token or Token is expired")











import datetime
from django.http import HttpRequest
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone
from main.utils.generate import generate_verification_token
from main.utils.shortcuts import get_verification_url
from main.utils.crud import save_verifcation_token
from main.forms import SignupStudentForm, SignupMerchantForm, LoginForm
from main.utils.generate import generate_wallet_id






# - AUTHENTICATIONS
async def signup_student(request:HttpRequest):

    form = SignupStudentForm()

    if request.method == "POST":

        form = SignupStudentForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id(10)

            current_user.is_student = True

            current_user.save()

            verification_token = generate_verification_token()

            expiration_time = timezone.now() + datetime.timedelta(minutes=3)

            save_verifcation_token(current_user.email, verification_token, expiration_time)

            verification_url = get_verification_url(request, verification_token)


            # send welcome mail

            # flash messages

            return redirect("home")
        
    context = {"form": form}

    return render(request, "registration/signup_student.html", context)


async def signup_merchants(request:HttpRequest):

    form = SignupMerchantForm()

    if request.method == "POST":
        form = SignupMerchantForm(request.POST)

        if form.is_valid():
            
            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id(10)

            current_user.is_merchant = True
    
            current_user.save()

            # Setup 2FA

            #create token

            # send welcome mail

            # flash messages

            return redirect("home")

    context = {"form": form}
    return render(request, "registration/signup_merchant.html", context)




def login(request:HttpRequest):
    
    if request.user.is_authenticated == True:


        if request.user.is_student:
            return redirect("dashboard_student")
        
        elif request.user.is_merchant:
            return redirect("dashboard_merchant")
   
    form = LoginForm()

    if request.method == "POST":
        
        email = request.POST.get("username")
        password = request.POST.get("password")

        
        user = authenticate(request, email=email, password=password)

        if user is not None and (user.is_verified):

            auth.login(request, user)
           
            if user.is_student:
                return redirect("dashboard_student")
        
            elif user.is_merchant:
                return redirect("dashboard_merchant")
        
        elif user is not None and (not user.is_verified):

            messages.error(request, "User is not Verified")
        else:
            
            messages.warning(request, "Email or password is incorrect")

    
    context = {"form":form}
    

    return render(request, "login/login_student.html", context)



def logout(request:HttpRequest):
    
    auth.logout(request)

    return redirect("login")




import datetime
from django.utils import timezone
from django.http import HttpRequest
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from utils.generate import generate_verification_token
from utils.shortcuts import get_verification_url, group_transactions_by_date, get_object_or_none
from utils.crud import save_verifcation_token
from utils.repsonse import CustomResponse
from utils.generate import generate_wallet_id
from main.models import CustomUser
from django.core.cache import cache
from Transactions.models import Transactions
from main.forms import SignupStudentForm, SignupMerchantForm, LoginForm

# - AUTHENTICATIONS
def signup_student(request:HttpRequest):

    form = SignupStudentForm()

    if request.method == "POST":

        form = SignupStudentForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id(10)

            current_user.is_student = True

            current_user.save()

            verification_token = generate_verification_token()

            expiration_time = timezone.now() + datetime.timedelta(minutes=30)

            save_verifcation_token(current_user.email, verification_token, expiration_time)

            verification_url = get_verification_url(request,current_user.email, verification_token)

            print(verification_url)
            # send welcome mail

            messages.success(request, "Verification Email has been sent")
            
            return redirect("signup_student")
        
    context = {"form": form}

    return render(request, "registration/signup_student.html", context)


def signup_merchant(request:HttpRequest):

    form = SignupMerchantForm()

    if request.method == "POST":
        form = SignupMerchantForm(request.POST)

        if form.is_valid():
            
            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id(10)

            current_user.is_merchant = True
    
            current_user.save()

            verification_token = generate_verification_token()

            expiration_time = timezone.now() + datetime.timedelta(minutes=3)

            save_verifcation_token(current_user.email, verification_token, expiration_time)

            verification_url = get_verification_url(request,current_user.email, verification_token)

            print(verification_url)

            messages.success(request, "Verification Email has been sent")

            # send welcome mail

            return redirect("signup_merchant")

    context = {"form": form}

    return render(request, "registration/signup_merchant.html", context)




def login(request:HttpRequest):

    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect("dashboard_student")
        elif request.user.is_merchant:
            return redirect("dashboard_merchant")
   
    form = LoginForm()

    if request.method == "POST":
        
        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_verified:
            prev_user_id = request.session.get('user_id', None)
            if prev_user_id:
                try:
                    prev_session = Session.objects.get(session_key=prev_user_id)
                    prev_session.delete()
                except Session.DoesNotExist:
                    pass

            # set the new user's session
            request.session['user_id'] = user.id
                    

            auth.login(request, user)
            

            if user.is_student:
                return redirect("dashboard_student")
            
            elif user.is_merchant:
                return redirect("dashboard_merchant")
            
            
            
        elif user is not None and not user.is_verified:
            messages.error(request, "User is not Verified")

        else:
            messages.warning(request, "Email or password is incorrect")

    context = {"form":form}

    return render(request, "login/login_student.html", context)



def logout(request:HttpRequest):
    
    auth.logout(request)

    return redirect("login")




@login_required(login_url="login")
def get_user(request:HttpRequest):

    data = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email
    }

    return CustomResponse("User Retrieved Successfull", data=data)


@login_required(login_url="login")
def dashboard_student(request:HttpRequest):
    

    if not request.user.is_student:
        return redirect("dashboard_merchant")
    

    trans_history = Transactions.objects.filter(sender=request.user).order_by("-date_added")

    transactions_by_date = group_transactions_by_date(trans_history)


    context = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "balance": request.user.balance,
        "wallet_id":request.user.wallet_id,
        "transactions_by_date": transactions_by_date
    }



    return render(request, "dashboard/dashboard_student.html", context)



@login_required(login_url="login")
def dashboard_merchant(request:HttpRequest):

    if not request.user.is_merchant:
        return redirect("dashboard_student")

    trans_history = Transactions.objects.filter(recipient=request.user).order_by("-date_added")


    transactions_by_date = group_transactions_by_date(trans_history)

    context = {
        "business_name": request.user.business_name,
        "last_name": request.user.last_name,
        "balance": request.user.balance,
        "wallet_id": request.user.wallet_id, 
        "transactions_by_date": transactions_by_date
    }

    return render(request, "dashboard/dashboard_merchants.html", context)




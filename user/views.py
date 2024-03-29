from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from utils.generate import generate_wallet_id
from utils.crud import fetchone
from utils.response import CustomResponse, BadRequest
from utils.mail import send_verification_mail, get_user_from_email_verification_token
from utils.shortcuts import redirect_not_student, redirect_not_merchant
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, MerchantRegistrationForm, LoginForm
# Create your views here.



def signup_student(request:HttpRequest):


    form = StudentRegistrationForm()

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id()

            current_user.save()


            send_verification_mail(request, current_user)


            messages.success(request, "Verification email has been sent")

            return redirect("signup_student")
    
    context = {"form": form}

    return render(request, "registration/signup_student.html", context)




def signup_merchant(request:HttpRequest):

    form = MerchantRegistrationForm()

    if request.method == "POST":
        form = MerchantRegistrationForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id()
            current_user.is_merchant = True

            current_user.save()

            send_verification_mail(request, current_user)


            messages.success(request, "Verification email has been sent")

            return redirect("signup_merchant")

    
    context = {"form": form}

    return render(request, "registration/signup_merchants.html", context)


def login(request:HttpRequest):

    if request.user.is_authenticated:
        if not request.user.is_merchant:
            return redirect("dashboard_student")
        else:
            return redirect("dashboard_merchant")

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:


                if not user.is_verified:
                    messages.warning(request, "Account not verified")

                    return redirect("login")

                else:
                    auth.login(request, user)

                    if not user.is_merchant:
                        return redirect("dashboard_student")
                    else:
                        return redirect("dashboard_merchant")

            else:
                messages.error(request, 'Email or password is incorrect')

    context = {"form":form}

    return render(request, "login/login.html", context)

    

@login_required(login_url="login")
@redirect_not_student
def dashboard_student(request:HttpRequest):

    context = {"user":request.user}

    return render(request, "dashboard/dashboard_student.html", context)




@login_required(login_url="login")
@redirect_not_merchant
def dashboard_merchant(request:HttpRequest):

    context = {"user":request.user}
    
    return render(request, "dashboard/dashboard_merchant.html", context)




@login_required(login_url="login")
def get_user_data(request:HttpRequest):
    
    return CustomResponse("Get User Data successfull", data=request.user.to_dict())




def request_verification(request:HttpRequest):

    if request.method == "POST":
        
        email = request.POST.get("email")

        user = fetchone(User, email=email)

        if user is not None:
            send_verification_mail(request, user)

            messages.success(request, "Verification email has been sent")

            return redirect("request_verification")
        
        else:
            messages.error(request, 'Email does not exists')

    return render(request, "verification/request_verification.html")




def verify_user(request:HttpRequest, uidb64, token):

    user = get_user_from_email_verification_token(uidb64, token)


    if user is None:

        messages.error(request, "Invalid Verification Link")

    if request.method == "POST":

        transaction_pin = request.POST.get("transaction_pin")

        if transaction_pin is None or  transaction_pin == "" or len(transaction_pin) != 4:
            return BadRequest("Please Check transaction pin")

        hashed_transaction_pin = make_password(transaction_pin)

        if user is not None:
            user.transaction_pin = hashed_transaction_pin
            user.is_verified = True

            user.save()

            auth.login(request, user)

            return CustomResponse("Account Verified")
        
        
    return render(request, "verification/verify_account.html")

        



def logout(request:HttpRequest):
    
    auth.logout(request)

    return redirect("login")



def choose_sign_student_merchant(request:HttpRequest):
    return render(request, "choose-student-merchant.html")



def http404(request:HttpRequest):
    return render(request, "404.html")
    
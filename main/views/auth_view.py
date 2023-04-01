from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from main.forms import SignupStudentForm, SignupMerchantForm, LoginForm
from main.models import CustomUser
from main.utils.generate import generate_wallet_id

from django.contrib import messages





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

            # Setup 2FA

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

        if user is not None:
            auth.login(request, user)
           

            if request.user.is_student:
                return redirect("dashboard_student")
        
            elif request.user.is_merchant:
                return redirect("dashboard_merchant")
            
        else:
            messages.warning(request, "Email or password is incorrect")

            
    context = {"form":form}

    return render(request, "login/login_student.html", context)



def logout(request:HttpRequest):
    
    auth.logout(request)

    return redirect("login")




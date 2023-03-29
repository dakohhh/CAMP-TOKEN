from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import SignupStudentForm, SignupMerchantForm, LoginForm

from .utils.generate import generate_wallet_id



from django.contrib import auth
from django.contrib.auth import authenticate





# Create your views here.





def home(request:HttpRequest):
 
    return render(request, "index.html")



def signup_student(request:HttpRequest):

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


def signup_merchants(request:HttpRequest):

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
    form = LoginForm()


    if request.method == "POST":
        
        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)

            # redirect to dashboard , confirm whether its student or merchant


    context = {"form":form}

    return render(request, "login/login_student.html", context)








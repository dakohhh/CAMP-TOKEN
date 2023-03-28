from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import SignupStudentForm, SignupMerchantForm

# Create your views here.





def home(request:HttpRequest):
 
    return render(request, "index.html")



def signup_student(request:HttpRequest):

    form = SignupStudentForm()

    if request.method == "POST":

        form = SignupStudentForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

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
            
            print(form.first_name, form.email)

            current_user = form.save(commit=False)

            form.save()

            # Setup 2FA

            # send welcome mail

            # flash messages

            return redirect("home")

    context = {"form": form}
    return render(request, "registration/signup_student.html", context)








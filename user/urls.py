from django.urls import path
from . import views

urlpatterns = [


    #SIGNUP STUDENT
    path("accounts/signup/student", views.signup_student, name="signup_student")

]
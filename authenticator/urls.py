from django.urls import path
from . import views


urlpatterns = [
    
    # - Home 

    path("", views.home, name="home"),

    # -   SIGNUP STUDENT
    path("accounts/signup/student", views.signup_student, name="signup_student"),

    # -  SIGNUP MERCHANT

    path("accounts/signup/merchant", views.signup_merchants, name="signup_merchant"),

    # -  LOGIN STUDENT

    path("accounts/login", views.login, name="login"),




    
]

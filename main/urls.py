from django.urls import path
from . import views





urlpatterns = [

    # - Home 

    path("", views.home, name="home"),

    # -  SIGNUP USER

    path("accounts/signup/user", views.signup_student, name="signup_user"),

    # -  SIGNUP MERCHANT

    path("accounts/signup/merchant", views.signup_merchants, name="signup_merchant"),

]
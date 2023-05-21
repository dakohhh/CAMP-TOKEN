from django.urls import path
from . import views

urlpatterns = [

    # SIGNUP STUDENT

    path("accounts/signup/student", views.signup_student, name="signup_student"),

    # SIGNUP MERCHANT

    path("accounts/signup/merchant", views.signup_merchant, name="signup_merchant"),

    path("accounts/choose", views.choose_sign_student_merchant, name="choose_sign_student_merchant")

]
from django.urls import path
from . import views

urlpatterns = [

    # SIGNUP STUDENT

    path("accounts/signup/student", views.signup_student, name="signup_student"),

    # SIGNUP MERCHANT

    path("accounts/signup/merchant", views.signup_merchant, name="signup_merchant"),

    # LOGIN

    path("accounts/login", views.login, name="login"),


    path("accounts/logout", views.logout, name="logout"),

    # SIGNUP CHOICE

    path("accounts/choose", views.choose_sign_student_merchant, name="choose_sign_student_merchant"),

    # DASHBOARD STUDENT

    path("dashboard/s/", views.dashboard_student, name="dashboard_student"),

    # DASHBOARD MERCHANT

    path("dashboard/m/", views.dashboard_merchant, name="dashboard_merchant"),

    # GET USER DATA
    path("get_user_data", views.get_user_data, name="get_user_data"),



    path("404", views.http404, name="404")

]
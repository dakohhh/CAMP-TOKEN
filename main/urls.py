from django.urls import path, re_path

from . import views

urlpatterns = [
    
    # -   SIGNUP STUDENT
    path("accounts/signup/student", views.signup_student, name="signup_student"),

    # -  SIGNUP MERCHANT

    path("accounts/signup/merchant", views.signup_merchant, name="signup_merchant"),

    # -  LOGIN STUDENT

    path("accounts/login", views.login, name="login"),

    # - LOGOUT 
    
    path("accounts/logout", views.logout, name="logout"),

    # VERIFY ACCOUNT

    # path("accounts/verify", verification_view.verify, name="verify"),

    # - DASHBOARD STUDENT

    path("dashboard/s/", views.dashboard_student, name="dashboard_student"),

    # - DASHBOARD MERCHANT

    path("dashboard/m/", views.dashboard_merchant, name="dashboard_merchant"),

    path("get_user", views.get_user, name="get_user"), 

    # re_path(r'^.*$', handle_404_error.custom_404_view),

]

from django.urls import path
from .views import auth_view
from .views import home_view
from .views import dashboard_view


urlpatterns = [
    
    # - Home 

    path("", home_view.home, name="home"),

    # -   SIGNUP STUDENT
    path("accounts/signup/student", auth_view.signup_student, name="signup_student"),

    # -  SIGNUP MERCHANT

    path("accounts/signup/merchant", auth_view.signup_merchants, name="signup_merchant"),

    # -  LOGIN STUDENT

    path("accounts/login", auth_view.login, name="login"),
    
    path("accounts/logout", auth_view.logout, name="logout"),

    # - DASHBOARD

    path("dashboard/s/", dashboard_view.dashboard_student, name="dashboard_student"),
    path("dashboard/m/", dashboard_view.dashboard_merchant, name="dashboard_merchant"),


]

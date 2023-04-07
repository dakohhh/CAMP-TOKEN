from django.urls import path
from .views import auth_view
from .views import home_view
from .views import dashboard_view
from .views import transaction_view


urlpatterns = [
    
    # - Home 

    path("", home_view.home, name="home"),

    # -   SIGNUP STUDENT
    path("accounts/signup/student", auth_view.signup_student, name="signup_student"),

    # -  SIGNUP MERCHANT

    path("accounts/signup/merchant", auth_view.signup_merchants, name="signup_merchant"),

    # -  LOGIN STUDENT

    path("accounts/login", auth_view.login, name="login"),

    # - LOGOUT 
    
    path("accounts/logout", auth_view.logout, name="logout"),

    # - DASHBOARD STUDENT

    path("dashboard/s/", dashboard_view.dashboard_student, name="dashboard_student"),

    # - DASHBOARD MERCHANT

    path("dashboard/m/", dashboard_view.dashboard_merchant, name="dashboard_merchant"),

    # - PAY A MERCHANT

    path("dashboard/s/pay", transaction_view.pay_merchant, name="pay_merchant"),

    # - CONFIRM MERCHANT 

    path("confirm_merchant_wallet_id", transaction_view.confirm_merchant_wallet_id, name="confirm_merchant_wallet_id"),

    # - PAY MERCHANT SUCCESS

    path("payments/success/<str:transaction_id>", transaction_view.payment_success, name="payment_merchant_success"),

    # - PAY MERCHANT FAILED

    path("payments/success/<str:transaction_id>", transaction_view.payment_failed, name="payment_merchant_failed"),


]

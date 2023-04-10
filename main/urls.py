from django.urls import path, re_path

from .views import auth_view
from .views import home_view
from .views import dashboard_view
from .views import transaction_view
from .views import handle_404_error


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

    path("/pay_merchant", transaction_view.pay_merchant, name="pay_merchant"),

    # - CONFIRM MERCHANT 

    path("confirm_merchant_wallet_id", transaction_view.confirm_merchant_wallet_id, name="confirm_merchant_wallet_id"),

    # - PAY MERCHANT STATUS SUCCESS OR FAILED

    path("pay_merchant/status/<str:transaction_id>", transaction_view.payment_merchant_status, name="payment_merchant_status"),

    # - REFUND STUDENT

    path("refund_student/<str:transaction_id>", transaction_view.refund_student, name="refund_student"), 

    # - REFUND STUDENT STATUS SUCCESS OR FAILED

    path("refund_student/status/<str:transaction_id>",transaction_view.refund_student_status, name="refund_student_status"), 

    re_path(r'^.*$', handle_404_error.custom_404_view),



]

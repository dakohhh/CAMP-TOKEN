from django.urls import path
from . import views

urlpatterns = [

    # PAY MERCHANT

    path("dashboard/s/pay", views.pay_merchant, name="pay_merchant"),

    # REFUND STUDENT

    path("dashboard/m/refund", views.refund_student, name="refund_student"),

    # CONFIRM MERCHANT WALLET

    path("confirm_merchant_wallet", views.confirm_merchant_wallet, name="confirm_merchant_wallet")

]
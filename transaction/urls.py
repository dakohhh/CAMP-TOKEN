from django.urls import path
from . import views

urlpatterns = [

    # PAY MERCHANT

    path("dashboard/s/pay", views.pay_merchant, name="pay_merchant"),

    # REFUND STUDENT

    path("dashboard/m/refund/<str:transaction_id>", views.refund_student, name="refund_student"),

    # CONFIRM MERCHANT WALLET

    path("confirm_merchant_wallet", views.confirm_merchant_wallet, name="confirm_merchant_wallet"),

    # GET ALL TRANSACTON FOR STUDENT

    path("get_student_transactions", views.get_student_transactions, name="get_student_transactions"),

]
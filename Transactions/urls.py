from django.urls import path

from . import views




urlpatterns = [
    path("pay_merchant", views.pay_merchant, name="pay_merchant"),

     # - FUND STUDENT WALLET

    path("fund_student_wallet", views.fund_student_wallet, name="fund_student_wallet"),
    
    # - CONFIRM MERCHANT 

    path("confirm_merchant_wallet_id", views.confirm_merchant_wallet_id, name="confirm_merchant_wallet_id"),

    # - PAY MERCHANT STATUS SUCCESS OR FAILED

    path("pay_merchant/status/<str:transaction_id>", views.payment_merchant_status, name="payment_merchant_status"),

    # - REFUND STUDENT

    path("refund_student/<str:transaction_id>", views.refund_student, name="refund_student"), 

    # - REFUND STUDENT STATUS SUCCESS OR FAILED

    path("refund_student/status/<str:transaction_id>",views.refund_student_status, name="refund_student_status"), 

]
from django.urls import path
from . import views

urlpatterns = [

    # SIGNUP STUDENT

    path("dashboard/s/pay", views.pay_merchant, name="pay_merchant"),


    path("dashboard/m/refund", views.refund_student, name="refund_student"),

]
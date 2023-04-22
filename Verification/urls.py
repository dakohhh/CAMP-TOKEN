from django.urls import path

from . import views

urlpatterns = [

    path("accounts/verify", views.verify, name="verify"),

    path("accounts/verify/resend", views.resend_verification, name="resend_verify"),
    

]
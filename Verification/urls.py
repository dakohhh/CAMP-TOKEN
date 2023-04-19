from django.urls import path

from . import views

urlpatterns = [

    path("accounts/verify", views.verify, name="verify"),

]
from django.urls import path
from . import views



urlpatterns = [

    # ADD MONEY

    path("dashboard/addmoney", views.add_money, name="add_money"),


    path("dashboard/addmoney/succss", views.add_money_success, name="add_money_success"),

]
from django.urls import path
from . import views





urlpatterns = [
    
    # - Home 

    path("", views.home, name="home"),

]
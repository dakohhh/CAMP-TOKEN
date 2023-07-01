import os
import requests
from django.http.request import HttpRequest
from django.urls import reverse
from utils.response import PaystackAPIException
from dotenv import load_dotenv
load_dotenv()



def add_money_request(request:HttpRequest, email:str, amount:int, trasaction_id:str):

    base = request.scheme + "://" + request.get_host()

    callback = base + reverse("dashboard_student")

    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {os.getenv('PAYSTACK_SECRET_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "amount": str(amount * 100),
        "reference": trasaction_id, 
        "callback_url" : callback
    }

    response = requests.post(url, headers=headers, json=data)


    if response.status_code == 200:
        return dict(response.json()).get("data")["authorization_url"]
    else:
        raise PaystackAPIException("Paystack API request failed")
    
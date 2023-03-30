

from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required




@login_required(login_url="login")
def dashboard(request:HttpRequest):
    
    return HttpResponse("workz")
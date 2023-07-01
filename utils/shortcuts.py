
from django.http import HttpRequest
from django.shortcuts import redirect





def redirect_not_student(view_func):
    
    def wrapper(request:HttpRequest, *args, **kwargs):

        if request.user.is_merchant:
            return redirect("dashboard_merchant")
        
        return view_func(request, *args, **kwargs)

    return wrapper



def redirect_not_merchant(view_func):
    
    def wrapper(request:HttpRequest, *args, **kwargs):

        if not request.user.is_merchant:
            return redirect("dashboard_student")
        
        return view_func(request, *args, **kwargs)

    return wrapper






from django.http.response import JsonResponse
from django.http import HttpResponse



class CustomResponse(JsonResponse):
    
    def __init__(self, msg, *args, status=200,  success=True, data=None, **kwargs) -> None:

        response = {
            "status": status, 
            "message" : msg,
            "success":success,
            "data": data
        }


        if kwargs != {}:
            response["extra_vals"] = kwargs


        super().__init__(data=response, status=status)




class NotFoundResponse(CustomResponse):
    def __init__(self, msg, data=None):
        super().__init__(msg, status=404, success=False, data=data)

    


class BadRequest(CustomResponse):
    def __init__(self, msg, data=None):
        super().__init__(msg, status=400, success=False, data=data)


class ServiceUnavailable(CustomResponse):
    def __init__(self, msg, data=None):
        super().__init__(msg, status=503, success=False, data=data)



class PaystackAPIException(Exception):
    pass






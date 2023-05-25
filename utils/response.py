from django.http.response import JsonResponse
from django.http import HttpResponse



class CustomResponse(JsonResponse):
    
    def __init__(self, msg, status=200, success=True, data=None) -> None:

        response = {
            "status": status, 
            "message" : msg,
            "success":success,
            "data": data
        }
        super().__init__(data=response, status=status)




class NotFoundResponse(CustomResponse):
    def __init__(self, msg):
        super().__init__(msg, status=404, success=False)

    


class BadRequest(CustomResponse):
    def __init__(self, msg):
        super().__init__(msg, status=400, success=False)






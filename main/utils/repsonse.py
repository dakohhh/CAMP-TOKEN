from django.http.response import JsonResponse








class CustomResponse(JsonResponse):
    
    def __init__(self, status, msg, success=True, data=None) -> None:

        data = {
        "status": status, 
        "msg" : msg,
        "success":success,
        "data": data
        }
        super().__init__(data=data, status=status)
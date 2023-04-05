from django.http.response import JsonResponse








class CustomResponse(JsonResponse):
    
    def __init__(self, msg, status=200, success=True, data=None) -> None:

        response = {
        "status": status, 
        "message" : msg,
        "success":success,
        "data": data
        }
        super().__init__(data=response, status=status)





class HttpResponseUnauthorized(CustomResponse):

    def __init__(self, msg) -> None:

        super().__init__(msg, status=401, success=False)


class HttpResponseNotFound(CustomResponse):

    def __init__(self, msg) -> None:

        super().__init__(msg, status=404, success=False)



class HttpResponseBadRequest(CustomResponse):

    def __init__(self, msg) -> None:

        super().__init__(msg, status=400,  success=False)


class HttpResponsePaymentRequired(CustomResponse):

    def __init__(self, msg) -> None:

        super().__init__(msg, status=402,  success=False)

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse


def hello(request):
    return HttpResponse('Hello Neal')


def login_by_password(request):
    return JsonResponse({
        "status": 0,
          "msg": "", 
          "data": "Login Success"
          })
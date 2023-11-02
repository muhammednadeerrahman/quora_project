import json

from django.urls import reverse
from django.http.response import HttpResponse,HttpResponseRedirect
from quora.models import Question,Answer


def allow_self(function):
    def wrapper(request, *args, **kwargs):
        id = kwargs["id"]
        if not Question.objects.filter(id=id,author__user = request.user).exists():
            if request.headers.get("x-requested-with")=="XMLHttpRequest":
                response_data = {
                    "title" : "unauthorised access",
                    "message" : "please check url",
                    "status"  : "error",
                }
                return HttpResponse(json.dumps(response_data),content_type = "application/json")
            else:
                return HttpResponseRedirect(reverse("web:index"))

        return function(request, *args, **kwargs)
    
    return wrapper

def allow_selfA(function):
    def wrapper(request, *args, **kwargs):
        id = kwargs["id"]
        if not Answer.objects.filter(id=id,author__user = request.user).exists():
            if request.headers.get("x-requested-with")=="XMLHttpRequest":
                response_data = {
                    "title" : "unauthorised access",
                    "message" : "please check url",
                    "status"  : "error",
                }
                return HttpResponse(json.dumps(response_data),content_type = "application/json")
            else:
                return HttpResponseRedirect(reverse("web:index"))

        return function(request, *args, **kwargs)
    
    return wrapper
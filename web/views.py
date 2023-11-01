from django.shortcuts import render
from quora.models import Question
from django.http.response import HttpResponse

def index (request):

    question = Question.objects.filter(is_deleted=False)
    context ={
        "title" : "quora",
        "question" : question
    }
    # return HttpResponse ("hello")
    return render(request, "web/index.html", context = context)
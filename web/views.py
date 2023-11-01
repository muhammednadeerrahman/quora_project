from django.shortcuts import render
from quora.models import Question, Answer
from django.http.response import HttpResponse

def index (request):

    question = Question.objects.filter(is_deleted=False)

    answer = Answer.objects.filter(is_deleted=False)

    context ={
        "title" : "quora",
        "question" : question,
        "answer" : answer,
    }
    # return HttpResponse ("hello")
    return render(request, "web/index.html", context = context)


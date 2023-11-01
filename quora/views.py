import json

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse

from quora.forms import QuestionForm, AnswerForm
from quora.models import Question, Answer
from main.functions import generate_form_errors


def create (request):
    if request.method == 'POST':
        name = request.user.profile
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            instance = form.save(commit=False)
            question = Question.objects.create(
                question = instance.question,
                name = name
            )
            response_data = {
                "message" :"sucessfully submitted",
                "title" :"sucessfully submitted",
                "status" : "success",
                "redirect_url" : "/",
                "redirect" : "yes"
            }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
        else:
            error_message = generate_form_errors(form)
            response_data = {
                    "message" :str(error_message),
                    "title" :"please check something error occured",
                    "status" : "error",
                    "redirect_url" : "/",
                    "redirect" : "yes"
                }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
    else: 
        form = QuestionForm()
        context ={
        "form" : form,
        "title" : "create form"
        }
    return render(request, "quora/create.html", context = context)

def answer(request,id):
    question = get_object_or_404(Question,id=id)
    username = request.user.profile
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            Answer.objects.create(
                question = question,
                username = username,
                answer = instance.answer

            )
            response_data = {
                "message" :"sucessfully submitted",
                "title" :"sucessfully submitted",
                "status" : "success",
                "redirect_url" : "/",
                "redirect" : "yes"
            }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
        else:
            error_message = generate_form_errors(form)
            response_data = {
                    "message" :str(error_message),
                    "title" :"please check something error occured",
                    "status" : "error",
                    "redirect_url" : "/",
                    "redirect" : "yes"
                }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
    else: 
        form = AnswerForm()
        context ={
        "form" : form,
        "title" : "create form"
        }
    return render(request,"quora/answer.html",context=context)
     

    #     question
    # if request.method == 'post':
    #     username = request.user.profile

    context = {
            "title" : "Write your Answer",
            "question" : question
        }
    return render(request,"quora/answer.html",context=context)
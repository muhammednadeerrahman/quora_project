import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from quora.forms import QuestionForm, AnswerForm
from quora.models import Question, Answer

from main.functions import generate_form_errors
from main.decorators import allow_self, allow_selfA

@login_required(login_url="/user/login/")
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
                    "error" : True,
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
        "title" : "create form",
        "request" : request
        }
    return render(request, "quora/create.html", context = context)


@login_required(login_url="/user/login/")
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
                    "error" : True,
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
        "title" : "create form",
        "question" : question
        }
    return render(request,"quora/answer.html",context=context)


@login_required(login_url="/user/login/")
@allow_self    
def deleteQ (request,id):

    instance = get_object_or_404(Question,id=id)
    instance.is_deleted = True
    instance.save()
    response_data = {
         "title" : "successfully deleted",
        "message" : "post deleted successfully",
        "status" : "success",
        "reload" : "yes",
    }
    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")


@login_required(login_url="/user/login/")
@allow_selfA
def deleteA (request,id):
    instance = get_object_or_404(Answer,id=id)
    instance.is_deleted = True
    instance.save()
    response_data = {
         "title" : "successfully deleted",
        "message" : "post deleted successfully",
        "status" : "success",
        "reload" : "yes",
    }
    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")

def like (request,id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Answer,id=id)
        if request.user in instance.like.all() :
            instance.like.remove(request.user)
            Like_status = False
        else:
            Like_status = True
            instance.like.add(request.user)
        instance.save()        
        like_count = str(instance.like.count()) + " likes"
        response_data = {
                "liked" : Like_status,
                "title": "Like toggled",
                "message": "Like status updated",
                "status": "success",
                "like_count": like_count ,
            }
    else:
        response_data = {
            "title": "Authentication required",
            "message": "Please log in to like answers",
            "status": "error",
        }
    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")

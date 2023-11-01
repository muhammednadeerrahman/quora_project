import json

from django.shortcuts import render
from django.http.response import HttpResponse

from quora.forms import QuestionForm
from quora.models import Question
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
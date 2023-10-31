from django.shortcuts import render, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django .contrib.auth.models import User

from user.forms import UserForm
from quora.models import Profile
from main.functions import generate_form_errors




def login (request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")   
    
        if username and password :
            user = authenticate(request, username = username, password = password )
            if user is not None :
                auth_login(request, user)
                return(HttpResponseRedirect("/"))
            
            context = {
                "title" : "login"
            }
            return render(request,"user/login.html",context=context)
    
    else:
        context = {
                "title" : "login"

        }
        return render (request, "user/login.html",context = context)
    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("user:login"))


def signup(request):
   if request.method == "POST" :
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            user = User.objects.create_user(
                username = instance.username,
                password = instance.password,
                first_name = instance.first_name,
                last_name = instance.last_name,
                email = instance.email,
            )
            Profile.objects.create(name = instance.first_name +" "+instance.last_name, email = instance.email, user=user)
            user = authenticate(request,username=instance.username, password=instance.password)
            auth_login(request, user)
            return HttpResponseRedirect(reverse("user:login"))
        else:
            message = generate_form_errors(form)
            context = {
                "title" : "user signup",
                "error" : True,
                "message" : message,
                "form" : form
            }
            return render(request, "user/signup.html",context = context)
   else:
      
    form = UserForm()
    context = {
        "title" : "user signup",
        "form" : form,
    }
    return render (request,"user/signup.html", context = context) 
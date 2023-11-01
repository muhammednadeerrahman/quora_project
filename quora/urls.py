from django.urls import path
from quora import views

app_name = "quora"

urlpatterns = [
    path('create/', views.create, name = "create"),

]
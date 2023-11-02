from django.urls import path
from quora import views

app_name = "quora"

urlpatterns = [
    path('create/', views.create, name = "create"),
    path('deleteQ/<int:id>', views.deleteQ, name = "deleteQ"),
    path('answer/<int:id>', views.answer, name = "answer"),
    path('like/<int:id>', views.like, name = "like"),
    path('deleteA/<int:id>', views.deleteA, name = "deleteA"),

]
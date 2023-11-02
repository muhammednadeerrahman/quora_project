from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["username","password","email","first_name","last_name",]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs={"placeholder" : "enter password","required" : "required"}),
             "username" : forms.widgets.TextInput(attrs = {"placeholder" : "enter username","required" : "required"}),
             "first_name" : forms.widgets.TextInput(attrs = {"placeholder" : "enter firstname","required" : "required"}),
             "last_name" : forms.widgets.TextInput(attrs = {"placeholder" : "enter lastname","required" : "required"}),
             "email" : forms.widgets.EmailInput(attrs = {"placeholder" : "enter email","required" : "required"}),
        }
        error_messages= {

            'first_name' : {
                "required" : "enter first name"
                },
            'last_name' : {
                    "required" : "enter last name"
                    },
            'email' : {
                    "required" : "select a email"
                    },
            'password' : {
                    "required" : "select a password"
                    },
        }
        

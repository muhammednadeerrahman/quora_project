from django import forms
from quora.models import Question

class QuestionForm(forms.ModelForm):
    
    class Meta :
        model = Question
        fields = ["question"]
        widgets = {
                "question" : forms.widgets.Textarea(attrs = {"placeholder" : "enter your question","required" : "required"}),
                }
        error_messages= {

                'question' : {
                    "required" : "question required"
                    },

            }
from django import forms
from quora.models import Question, Answer

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
        
class AnswerForm(forms.ModelForm):
    class Meta :
        model = Answer
        fields = ["answer"]
        widgets = {
                "Answer" : forms.widgets.Textarea(attrs = {"placeholder" : "write your answer","required" : "required"}),
                }
        error_messages= {

                'Answer' : {
                    "required" : "answer required"
                    },

            }
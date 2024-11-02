from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['response']
        widgets = {
            'response': forms.Textarea(attrs={'placeholder': '답변을 입력해주세요'}),
        }

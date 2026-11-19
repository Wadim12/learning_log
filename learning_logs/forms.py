from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text", "description"]
        widgets = {
            "text": forms.TextInput(attrs={"placeholder": "Например, Python"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Кратко опишите, чему хотите научиться"}),
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        widgets = {"text": forms.Textarea(attrs={"rows": 7, "placeholder": "Запишите, что нового вы узнали..."})}

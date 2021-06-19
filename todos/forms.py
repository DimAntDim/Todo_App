from django import forms
from django.forms.widgets import Textarea


class CreateTodo(forms.Form):
    creator = forms.CharField(max_length=20)
    status = forms.BooleanField()
    description = forms.CharField(
        widget=Textarea,
    )
    date = forms.DateTimeField()

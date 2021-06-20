from django import forms
from django.forms.widgets import Textarea


class CreateTodoForm(forms.Form):
    owner = forms.CharField(
        max_length=20,
        )

    text = forms.CharField(
        max_length=20,
        )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                'class': 'my-text-area',
            }
        )
    )

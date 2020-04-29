
from django import forms
from .models import Destination


class MyForm(forms.ModelForm):

    class Meta:
        model = Destination
        fields = ['name', 'img', 'desc', 'cont']

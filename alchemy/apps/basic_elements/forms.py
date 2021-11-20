from django import forms
from .models import BasicElement

class BasicElementCreateForm(forms.ModelForm):
    class Meta:
        model=BasicElement
        fields=['name','value']
        labels={'name':'Nombre del elemento',
                'value':'Valor del elemento'}
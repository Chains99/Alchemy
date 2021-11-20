from django import forms
from .models import Subject

class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name']
        labels={'name':'Nombre de la asignatura'}
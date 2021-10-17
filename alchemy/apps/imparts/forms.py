from django import forms
from .models import Imparts

class ImpartsCreateForm(forms.ModelForm):
    class Meta:
        model=Imparts
        fields=['professor']
        labels={'professor':'Profesor'}
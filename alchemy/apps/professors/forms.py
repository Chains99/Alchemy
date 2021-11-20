from django.contrib.auth.forms import UserCreationForm
from .models import Professor
from django.forms import CharField,PasswordInput

class ProfessorRegisterForm(UserCreationForm):
    password1=CharField(label='Contraseña',widget=PasswordInput)
    password2=CharField(label='Contraseña',widget=PasswordInput)    

    class Meta:
        model=Professor
        fields=['username','first_name','last_name','email','password1','password2']
        help_texts={k:"" for k in fields}
        labels={
            'username': 'Alias',
            'first_name': 'Nombre',
            'last_name':'Apellidos',
            'email':'Correo electrónico',
            'password1':'Contraseña',
            'password2':'Confirmar contraseña'
        }
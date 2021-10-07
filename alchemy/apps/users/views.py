from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserEditForm

class UserUpdate(UpdateView):
    model=User
    form_class=UserEditForm
    template_name='register_user.html'
    success_url=reverse_lazy('index')
    permission_required='students.change_student'
    permission_denied_message='Acceso denegado. Usuario no autorizado'
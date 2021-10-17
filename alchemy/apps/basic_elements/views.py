from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .models import BasicElement
from .forms import BasicElementCreateForm

class BasicElementList(ListView,PermissionRequiredMixin):
    model=BasicElement
    template_name='basic_element.html'
    permission_required='basic_elements.view_basic_element'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class BasicElementCreate(CreateView,PermissionRequiredMixin):
    form_class=BasicElementCreateForm
    template_name='create_basic_element.html'
    permission_required='basic_elements.add_basic_element'
    permission_denied_message='Acceso denegado. Usuario no autorizado'
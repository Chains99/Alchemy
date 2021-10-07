from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Subject
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from apps.imparts.models import Imparts
from .forms import SubjectCreateForm
from django.urls import reverse_lazy

class SubjectList(ListView,PermissionRequiredMixin):
    model=Subject
    template_name='subjects.html'
    permission_required='subjects.view_subject'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class SubjectCreate(CreateView,PermissionRequiredMixin):
    model=Subject
    form_class=SubjectCreateForm
    template_name='create_subject.html'
    success_url=reverse_lazy('subjects')
    permission_required='subjects.add_subject'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class SubjectUpdate(UpdateView,PermissionRequiredMixin):
    model=Subject
    form_class=SubjectCreateForm
    template_name='create_subject.html'
    success_url=reverse_lazy('subjects')
    permission_required='subjects.change_subject'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class SubjectDelete(PermissionRequiredMixin,DeleteView):
    model=Subject
    template_name='delete_subject.html'
    success_url=reverse_lazy('subjects')
    permission_required='subjects.delete_subject'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

def professor_or_student(request,pk):
    try:
        Imparts.objects.get(subject=pk,professor=request.user.id)
    except:
        return redirect('subject_student',pk)
    return redirect('subject_professor',pk)
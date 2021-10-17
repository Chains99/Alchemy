from apps.students.models import Student
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Subject
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from apps.imparts.models import Imparts
from .forms import SubjectCreateForm
from django.urls import reverse_lazy
from apps.admins.models import Admin
from apps.study.models import Study
from django.http import HttpResponseForbidden

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

def professor_or_student_or_admin(request,pk):
    try:
        Admin.objects.get(id=request.user.id)
    except:
        try:
            Imparts.objects.get(subject=pk,professor=request.user.id)
        except:
            try:
                Study.objects.get(subject=pk,student=request.user.id)
            except:
                try:
                    Student.objects.get(id=request.user.id)
                except:
                    return HttpResponseForbidden()
                return redirect('enroll',pk)
            return redirect('subject_student',pk)
        return redirect('subject_professor',pk)
    return redirect('subject_admin',pk)
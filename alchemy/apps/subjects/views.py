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
from apps.professors.models import Professor

class SubjectList(PermissionRequiredMixin,ListView):
    model=Subject
    template_name='subjects.html'
    permission_required='subjects.view_subject'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

    def get_context_data(self):
        user=self.request.user.id
        try:
            Professor.objects.get(id=user)
        except :
            subjects=Subject.objects.all()
            return {'subjects':subjects}
        subjects=[]
        for imparts in Imparts.objects.filter(professor=user):
            subjects.append(imparts.subject)
        return {'subjects':subjects}

class SubjectCreate(PermissionRequiredMixin,CreateView):
    model=Subject
    form_class=SubjectCreateForm
    template_name='create_subject.html'
    success_url=reverse_lazy('subjects')
    permission_required='subjects.add_subject'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class SubjectUpdate(PermissionRequiredMixin,UpdateView):
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
    if(request.user.is_superuser):
        return redirect('subject_admin',pk)
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
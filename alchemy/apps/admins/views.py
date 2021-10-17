from django.shortcuts import render
from .forms import AdminRegisterForm
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Admin
from apps.professors.models import Professor
from apps.subjects.models import Subject
from apps.imparts.models import Imparts
from apps.students.models import Student
from apps.study.models import Study


class AdminList(ListView,PermissionRequiredMixin):
    model=Admin
    template_name='admins.html'
    permission_required='admins.view_admin'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class AdminCreate(CreateView,PermissionRequiredMixin):
    form_class=AdminRegisterForm
    template_name='register_user.html'
    permission_required='admins.add_admin'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

    def form_valid(self,form):
        user=form.save()

        permissions=['add','view','change','delete']
        
        for perm in permissions:
            content_type=ContentType.objects.get_for_model(Admin)
            permission=Permission.objects.get(
                codename=perm+'_'+'admin',
                content_type=content_type
            )
            user.user_permissions.add(permission)

            content_type=ContentType.objects.get_for_model(Subject)
            permission=Permission.objects.get(
                codename=perm+'_'+'subject',
                content_type=content_type
            )
            user.user_permissions.add(permission)

            content_type=ContentType.objects.get_for_model(Professor)
            permission=Permission.objects.get(
                codename=perm+'_'+'professor',
                content_type=content_type
            )
            user.user_permissions.add(permission)

            content_type=ContentType.objects.get_for_model(Imparts)
            permission=Permission.objects.get(
                codename=perm+'_'+'imparts',
                content_type=content_type
            )
            user.user_permissions.add(permission)

            content_type=ContentType.objects.get_for_model(Student)
            permission=Permission.objects.get(
                codename=perm+'_'+'student',
                content_type=content_type
            )
            user.user_permissions.add(permission)

            content_type=ContentType.objects.get_for_model(Study)
            permission=Permission.objects.get(
                codename=perm+'_'+'study',
                content_type=content_type
            )
            user.user_permissions.add(permission)

        return HttpResponseRedirect(reverse_lazy('index'))

class AdminDelete(DeleteView,PermissionRequiredMixin):
    model=Admin
    template_name='delete_user.html'
    success_url=reverse_lazy('admins')
    permission_required='admins.delete_admin'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

def list(request,pk):
    imparts_subject=Imparts.objects.filter(subject=pk)
    study_subject=Study.objects.filter(subject=pk)

    imparts=[]
    study=[]

    for imsu in imparts_subject:
        imparts.append(str(pk)+'_'+str(imsu.professor.id))
    
    for stsu in study_subject:
        study.append(str(pk)+'_'+str(stsu.student.id))

    context={
        'pk':pk,
        'imparts':zip(imparts_subject,imparts),
        'study':zip(study_subject,study),
    }

    return render(request,'subject_admin.html',context)

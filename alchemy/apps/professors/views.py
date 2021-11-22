from apps.admins.models import Admin
from .forms import ProfessorRegisterForm
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Professor
from apps.basic_elements.models import BasicElement
from apps.subjects.models import Subject

class ProfessorList(PermissionRequiredMixin,ListView):
    model=Professor
    template_name='professors.html'
    permission_required='professors.view_professor'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

class ProfessorCreate(PermissionRequiredMixin,CreateView):
    form_class=ProfessorRegisterForm
    template_name='register_user.html'
    permission_required='professors.add_professor'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

    def form_valid(self,form):
        user=form.save()

        permissions=['add','view','change','delete']
        
        for perm in permissions:
            content_type=ContentType.objects.get_for_model(BasicElement)
            permission=Permission.objects.get(
                codename=perm+'_'+'basicelement',
                content_type=content_type
            )
            user.user_permissions.add(permission)

        content_type=ContentType.objects.get_for_model(Subject)
        permission=Permission.objects.get(
            codename='view_subject',
            content_type=content_type
            )
        user.user_permissions.add(permission)

        content_type=ContentType.objects.get_for_model(Professor)
        permission=Permission.objects.get(
            codename='change_professor',
            content_type=content_type
            )
        user.user_permissions.add(permission)

        content_type=ContentType.objects.get_for_model(Admin)
        permission=Permission.objects.get(
            codename='view_admin',
            content_type=content_type
            )
        user.user_permissions.add(permission)

        return HttpResponseRedirect(reverse_lazy('professors'))

class ProfessorDelete(PermissionRequiredMixin,DeleteView):
    model=Professor
    template_name='delete_user.html'
    success_url=reverse_lazy('professors')
    permission_required='professors.delete_profesor'
    permission_denied_message='Acceso denegado. Usuario no autorizado'
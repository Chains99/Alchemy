from .forms import StudentRegisterForm
from django.views.generic import CreateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Student
from apps.non_basic_elements.models import NonBasicElement
from apps.subjects.models import Subject

class StudentList(ListView,PermissionRequiredMixin):
    model=Student
    template_name='students.html'
    permission_required='students.view_student'
    permission_denied_message='Acceso denegado. Usuario no autorizado'


class StudentCreate(CreateView):
    form_class=StudentRegisterForm
    template_name='register_user.html'

    def form_valid(self,form):
        user=form.save()

        content_type=ContentType.objects.get_for_model(Student)
        permission=Permission.objects.get(
            codename='change_student',
            content_type=content_type
            )
        user.user_permissions.add(permission)

        content_type=ContentType.objects.get_for_model(Subject)
        permission=Permission.objects.get(
            codename='view_subject',
            content_type=content_type
            )
        user.user_permissions.add(permission)

        content_type=ContentType.objects.get_for_model(NonBasicElement)
        permission=Permission.objects.get(
            codename='add_nonbasicelement',
            content_type=content_type
            )
        user.user_permissions.add(permission)

        return HttpResponseRedirect(reverse_lazy('index'))

class StudentDelete(DeleteView,PermissionRequiredMixin):
    model=Student
    template_name='delete_user.html'
    success_url=reverse_lazy('students')
    permission_required='students.delete_student'
    permission_denied_message='Acceso denegado. Usuario no autorizado'
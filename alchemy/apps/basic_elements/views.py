from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView,UpdateView
from datetime import datetime
from apps.imparts.models import Imparts
from .models import BasicElement
from .forms import BasicElementCreateForm

@permission_required('basic_elements.view_basicelement')
def basic_element_list(request,pk):
    basic_elements=BasicElement.objects.filter(imparts__subject=pk)
    return render(request,'basic_elements.html',{'pk':pk,'basic_elements':basic_elements})

class BasicElementCreate(PermissionRequiredMixin,CreateView):
    model=BasicElement
    form_class=BasicElementCreateForm
    template_name='create_basic_element.html'
    permission_required='basic_elements.addbasicelement'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

    def form_valid(self,form):
        pk = self.kwargs.get(self.pk_url_kwarg)
        basic_elment=form.save(commit=False)
        basic_elment.imparts=Imparts.objects.get(professor=self.request.user.id,subject=pk)
        basic_elment.date_time_creation=datetime.now()
        basic_elment.save()
        return HttpResponseRedirect(reverse_lazy('basic_elements',kwargs={'pk':pk}))

@permission_required('basic_elements.change_basicelement')
def make_visible(request,pk):
    basic_element=BasicElement.objects.get(id=pk)
    basic_element.visible=True
    basic_element.save()
    subject=basic_element.imparts.subject.id
    return redirect('basic_elements',subject)

class BasicElementEdit(PermissionRequiredMixin,UpdateView):
    model=BasicElement
    form_class=BasicElementCreateForm
    template_name='create_basic_element.html'
    permission_required='basic_elements.change_basic_element'
    permission_denied_message='Acceso denegado. Usuario no autorizado'

    def form_valid(self,form):
        basic_element=form.save()
        pk=basic_element.imparts.subject.id
        return HttpResponseRedirect(reverse_lazy('basic_elements',kwargs={'pk':pk}))

@permission_required('basic_elements.delete_basicelement')
def delete_basic_element(request,pk):
    basic_element=BasicElement.objects.get(id=pk)
    if request.method=='GET':
        context={
            'basic_element':basic_element
        }
    else:
        basic_element.delete()
        subject=basic_element.imparts.subject.id
        return redirect('basic_elements',pk=subject)
    return render(request,'delete_basic_element.html',context)
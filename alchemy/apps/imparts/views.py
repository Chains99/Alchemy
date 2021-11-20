from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from apps.subjects.models import Subject
from django.shortcuts import render,redirect
from .models import Imparts
from .forms import ImpartsCreateForm
from apps.non_basic_elements.models import NonBasicElement

def create_imparts(request,pk):  
    if request.method=='GET':
        form=ImpartsCreateForm()
        context={
            'form':form
        }
    else:
        form=ImpartsCreateForm(request.POST)
        context={
            'form':form
        }
        imparts=Imparts()
        if form.is_valid():
            imparts.subject=Subject.objects.get(id=pk)
            imparts.professor=form.cleaned_data.get('professor')
            imparts.save()
            return redirect('subject_admin',pk=pk)
    return render(request,'create_imparts.html',context)

def delete_imparts(request,pk):
    imparts=Imparts.objects.get(id=pk)
    if request.method=='GET':
        context={
            'imparts':imparts
        }
    else:
        imparts.delete()
        subject=imparts.subject.id
        return redirect('subject_admin',pk=subject)
    return render(request,'delete_imparts.html',context)

def request_list(request,pk):
    requests=NonBasicElement.objects.filter(accepted=False,study__subject=pk)
    context={
        'requests' : requests,
        'pk' : pk
    }
    return render(request,'subject_professor.html',context)
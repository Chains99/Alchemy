from apps.professors.models import Professor
from apps.subjects.models import Subject
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render,redirect
from .models import Imparts
from .forms import ImpartsCreateForm

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
    str_subject,str_professor=pk.split('_')
    subject=int(str_subject)
    professor=int(str_professor)
    imparts=Imparts.objects.get(subject=subject,professor=professor)
    imparts.my_delete(subject,professor)
    return redirect('subject_admin',subject)
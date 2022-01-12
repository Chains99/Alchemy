from django import forms
from django.contrib.auth.decorators import permission_required
from apps.subjects.models import Subject
from django.shortcuts import render,redirect
from .models import Imparts
from apps.professors.models import Professor
from apps.non_basic_elements.models import NonBasicElement
from apps.basic_elements.models import BasicElement

@permission_required('imparts.add_imparts')
def create_imparts(request,pk):

    professors_subject=Imparts.objects.filter(subject=pk).exclude(professor__isnull=True)
    ps=set([(imparts.professor.id,imparts.professor.username) for imparts in professors_subject])
    
    professors=Professor.objects.all()
    p=set([(professor.id,professor.username) for professor in professors])

    profs=p.difference(ps)

    class ImpartsCreateForm(forms.Form):       
        professor=forms.ChoiceField(choices=profs,label='Profesor')

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
            imparts.professor=Professor.objects.get(id=form.cleaned_data.get('professor'))
            imparts.save()
            return redirect('subject_admin',pk=pk)
    return render(request,'create_imparts.html',context)

@permission_required('imparts.delete_imparts')
def delete_imparts(request,pk):
    imparts=Imparts.objects.get(id=pk)
    if request.method=='GET':
        context={
            'imparts':imparts
        }
    else:
        subject=imparts.subject.id
        elements_created=BasicElement.objects.filter(imparts__id=pk)
        if len(elements_created)==0:
            imparts.delete()
        else:
            imparts.professor=None
            imparts.save()
        return redirect('subject_admin',pk=subject)
    return render(request,'delete_imparts.html',context)

@permission_required('basic_elements.add_basicelement')
def request_list(request,pk):
    imparts=Imparts.objects.get(subject=pk,professor=request.user.id)
    requests=NonBasicElement.objects.filter(accepted=False,study__subject=pk)
    context={
        'requests' : requests,
        'imparts': imparts
    }
    return render(request,'subject_professor.html',context)
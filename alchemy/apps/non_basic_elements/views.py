from django.shortcuts import redirect, render
from datetime import datetime
from apps.study.models import Study
from .models import NonBasicElement
from django import forms
from .models import NonBasicElement
from apps.basic_elements.models import BasicElement
from apps.elements.models import Element
from django.contrib.auth.decorators import permission_required

@permission_required('non_basic_elements.view_nonbasicelement')
def accepted_list(request,pk):
    study=Study.objects.get(subject=pk,student=request.user.id)
    non_basic_elements=NonBasicElement.objects.filter(study=study.id).filter(accepted=True)
    return render(request,'accepted_list.html',{'study':study,'non_basic_elements':non_basic_elements})

@permission_required('non_basic_elements.view_nonbasicelement')
def pending_list(request,pk):
    study=Study.objects.get(subject=pk,student=request.user.id)
    non_basic_elements=NonBasicElement.objects.filter(study=study.id).filter(accepted=False)
    return render(request,'pending_list.html',{'study':study,'non_basic_elements':non_basic_elements})

def create_form(request, choices):
      
    class NonBasicElementCreateForm(forms.Form):
        name=forms.CharField(max_length=100,label='Nombre')
        element1=forms.ChoiceField(choices=choices,label='Elemento 1')
        element2=forms.ChoiceField(choices=choices,label='Elemento 2')
        justification=forms.CharField(widget=forms.Textarea,max_length=1000,label='Justificación')

    form=NonBasicElementCreateForm() if request.method=='GET' else NonBasicElementCreateForm(request.POST)
    return form

@permission_required('non_basic_elements.add_nonbasicelement')
def create_non_basic_element(request,pk):
    study=Study.objects.get(student=request.user.id,subject=pk)
    non_basic_elements=NonBasicElement.objects.filter(study=study,accepted=True)
    basic_elements=BasicElement.objects.filter(imparts__subject=pk,visible=True)

    choices=[]
    for element in basic_elements:
        choices.append((element.id,element.name))

    for element in non_basic_elements:
        choices.append((element.id,element.name))
        
    if request.method=='GET':
        form=create_form(request, choices)
        contexto={
            'form':form
        }
    else:
        form=create_form(request, choices)
        contexto={
            'form':form
        }
        if form.is_valid():
            non_basic_element=NonBasicElement()
            non_basic_element.study=study
            non_basic_element.date_time_creation=datetime.now()
            non_basic_element.name=form.cleaned_data.get('name')
            non_basic_element.justification=form.cleaned_data.get('justification')
            non_basic_element.element1=Element.objects.get(id=form.cleaned_data.get("element1"))
            non_basic_element.element2=Element.objects.get(id=form.cleaned_data.get("element2"))
            non_basic_element.value=non_basic_element.element1.value+non_basic_element.element2.value
            non_basic_element.save()
            return redirect('subject_student',pk=pk)

    return render(request,'create_non_basic_element.html',contexto)

@permission_required('non_basic_elements.delete_nonbasicelement')
def delete_non_basic_element(request,pk):
    non_basic_element=NonBasicElement.objects.get(id=pk)
    if request.method=='GET':
        context={
            'non_basic_element':non_basic_element
        }
    else:
        non_basic_element.delete()
        subject=non_basic_element.study.subject.id
        return redirect('pending_list',pk=subject)
    return render(request,'delete_non_basic_element.html',context)

@permission_required('basic_elements.add_basicelement')
def reject_non_basic_element(request,pk):
    non_basic_element=NonBasicElement.objects.get(id=pk)
    if request.method=='GET':
        context={
            'non_basic_element':non_basic_element
        }
    else:
        non_basic_element.delete()
        subject=non_basic_element.study.subject.id
        return redirect('subject_professor',pk=subject)
    return render(request,'reject_element.html',context)

@permission_required('basic_elements.add_basicelement')
def accept_non_basic_element(request,pk):
    non_basic_element=NonBasicElement.objects.get(id=pk)
    if request.method=='GET':
        context={
            'non_basic_element':non_basic_element
        }
    else:
        non_basic_element.accepted=True
        non_basic_element.study.student.credits+=non_basic_element.value
        non_basic_element.study.credits+=non_basic_element.value
        non_basic_element.save()
        non_basic_element.study.save()
        non_basic_element.study.student.save()
        subject=non_basic_element.study.subject.id
        return redirect('subject_professor',pk=subject)
    return render(request,'accept_element.html',context)
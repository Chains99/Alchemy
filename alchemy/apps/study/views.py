from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,redirect
from apps.students.models import Student
from .models import Study
from apps.subjects.models import Subject
from apps.imparts.models import Imparts

@permission_required('non_basic_elements.view_nonbasicelement')
def subject_student(request,pk):
    student=request.user.id
    study=Study.objects.get(subject=pk,student=student)
    imparts=Imparts.objects.filter(subject=pk).exclude(professor__isnull=True)
    context={
        'study':study,
        'imparts':imparts
    }
    return render(request,'subject_student.html',context)

@permission_required('non_basic_elements.view_nonbasicelement')
def enroll(request,pk):  
    if request.method=='GET':
        context={
            'subject': Subject.objects.get(id=pk)
        }
    else:
        study=Study()
        study.subject=Subject.objects.get(id=pk)
        study.student=Student.objects.get(id=request.user.id)
        study.save()
        return redirect('subject_student',pk=pk)
    return render(request,'enroll.html',context)

@permission_required('study.delete_study')
def delete_study(request,pk):
    study=Study.objects.get(id=pk)
    if request.method=='GET':
        context={
            'study':study
        }
    else:
        study.delete()
        subject=study.subject.id
        return redirect('subject_admin',pk=subject)
    return render(request,'delete_study.html',context)
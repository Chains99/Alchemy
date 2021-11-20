from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from apps.students.models import Student
from .models import Study
from apps.subjects.models import Subject

def subject_student(request,pk):
    student=request.user.id;
    study=Study.objects.get(subject=pk,student=student)
    context={
        'study':study
    }
    return render(request,'subject_student.html',context)

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
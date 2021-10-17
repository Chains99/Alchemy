from django.shortcuts import render,redirect
from apps.students.models import Student
from .models import Study
from apps.subjects.models import Subject

def subject_student(request,pk):

    return render(request,'index.html')

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
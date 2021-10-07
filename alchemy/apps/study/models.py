from apps.subjects.models import Subject
from django.db import models
from apps.students.models import Student
from apps.subjects.models import Subject
from cpkmodel import CPkModel

class Study(CPkModel):
    student=models.OneToOneField(Student,models.CASCADE,primary_key=True)
    subject=models.OneToOneField(Subject,models.CASCADE,primary_key=True)
    credits=models.IntegerField(default=0)

    class Meta:
        managed=False
        unique_together=(('student','subject'),)
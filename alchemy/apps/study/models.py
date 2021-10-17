from apps.subjects.models import Subject
from django.db import models
from apps.students.models import Student
from apps.subjects.models import Subject

class Study(models.Model):
    id=models.AutoField(primary_key=True)
    student=models.ForeignKey(Student,models.CASCADE,default=0)
    subject=models.ForeignKey(Subject,models.CASCADE,default=0)
    credits=models.IntegerField(default=0)

    class Meta:
        unique_together=(('student','subject'),)
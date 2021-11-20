from django.db import models
from apps.professors.models import Professor
from apps.subjects.models import Subject
from django.db import models

class Imparts(models.Model):
    id=models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, models.SET_NULL,default=0,null=True)
    subject = models.ForeignKey(Subject, models.CASCADE,default=0) 

    class Meta:
        unique_together = (('professor','subject'),)
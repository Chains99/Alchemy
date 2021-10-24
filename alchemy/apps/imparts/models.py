from django.db import models
from apps.professors.models import Professor
from apps.subjects.models import Subject
from django.db import models
from django.db import connection

class Imparts(models.Model):
    id=models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, models.CASCADE,default=0)
    subject = models.ForeignKey(Subject, models.CASCADE,default=0) 

    class Meta:
        unique_together = (('professor','subject'),)
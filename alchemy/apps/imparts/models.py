from django.db import models
from apps.professors.models import Professor
from apps.subjects.models import Subject
from django.db import models
from cpkmodel import CPkModel

class Imparts(CPkModel):
    subject = models.OneToOneField(Subject, models.CASCADE, primary_key=True) 
    professor = models.OneToOneField(Professor, models.CASCADE, primary_key=True)

    class Meta:
        managed=False
        unique_together = (('subject', 'professor'),)
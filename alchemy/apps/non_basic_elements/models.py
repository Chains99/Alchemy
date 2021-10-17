from django.db import models
from apps.study.models import Study
from apps.elements.models import Element

class NonBasicElement(Element):
    subject=models.IntegerField()
    student=models.IntegerField()
    element1=models.ForeignKey(Element,models.DO_NOTHING, related_name='nonBasicElement_element1')
    element2=models.ForeignKey(Element,models.DO_NOTHING, related_name='nonBasicElement_element2')
    justification=models.CharField(max_length=1000)
    study=models.OneToOneField(Study,models.CASCADE,related_name='nonBasicElement_study')

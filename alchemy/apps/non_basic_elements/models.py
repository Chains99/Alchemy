from django.db import models
from apps.study.models import Study
from compositefk.fields import CompositeForeignKey
from apps.elements.models import Element

class NonBasicElement(Element):
    subject=models.IntegerField()
    student=models.IntegerField()
    element1=models.OneToOneField(Element,models.DO_NOTHING, related_name='nonBasicElement_element1')
    element2=models.OneToOneField(Element,models.DO_NOTHING, related_name='nonBasicElement_element2')
    justification=models.CharField(max_length=1000)
    study=CompositeForeignKey(Study,on_delete=models.CASCADE,related_name='nonBasicElement_study',to_fields={
        'subject':'subject',
        'student':'student'
    })

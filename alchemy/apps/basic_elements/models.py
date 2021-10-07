from django.db import models
from apps.elements.models import Element
from django.db.models.deletion import DO_NOTHING
from compositefk.fields import CompositeForeignKey
from apps.imparts.models import Imparts

class BasicElement(Element):
    subject = models.IntegerField()
    professor = models.IntegerField()

    imparts=CompositeForeignKey(Imparts,on_delete=DO_NOTHING,related_name='basicElement_imparts',to_fields={
        'subject':'subject',
        'professor':'professor'
    })
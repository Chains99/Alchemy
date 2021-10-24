from django.db import models
from apps.elements.models import Element
from django.db.models.deletion import DO_NOTHING
from apps.imparts.models import Imparts

class BasicElement(Element):
    visible=models.BooleanField(default=False)
    imparts=models.ForeignKey(Imparts,DO_NOTHING,related_name='basicElement_imparts')
from django.db import models
from apps.elements.models import Element
from django.db import models
from apps.imparts.models import Imparts

class BasicElement(Element):
    visible=models.BooleanField(default=False)
    imparts=models.ForeignKey(Imparts,models.CASCADE,related_name='basicElement_imparts',default=0)

    def __str__(self) -> str:
        return self.name

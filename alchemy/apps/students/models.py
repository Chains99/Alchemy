from django.contrib.auth.models import User
from django.db.models.fields import IntegerField

class Student(User):
    credits=IntegerField(default=0)

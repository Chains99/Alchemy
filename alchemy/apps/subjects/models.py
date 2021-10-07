from django.db import models

class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)

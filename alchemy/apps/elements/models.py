from django.db import models

class Element(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    value=models.IntegerField()
    date_time_creation=models.DateTimeField()

    def __str__(self) -> str:
        return self.name

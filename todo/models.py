from django.db import models

# Create your models here.
class Task(models.Model) :
    name=models.CharField(max_length=20)
    namenoneed=models.CharField(max_length=20,null=True)
    description=models.TextField(null=True)
    status=models.BooleanField(default=False)
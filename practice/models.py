from django.db import models

# Create your models here.
class addition(models.Model):
    number1=models.IntegerField()
    number2=models.IntegerField()
    result=models.IntegerField()

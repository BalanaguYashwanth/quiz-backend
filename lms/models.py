from django.db import models

# Create your models here.
class verify(models.Model):
    questions=models.TextField()
    answers=models.TextField()


class quiz(models.Model):
    q=models.TextField()
    a=models.TextField()
    b=models.TextField()
    c=models.TextField()
    d=models.TextField()

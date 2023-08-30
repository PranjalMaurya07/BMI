from django.db import models

# Create your models here.
class bmi(models.Model):
    weight=models.CharField(max_length=3)
    height=models.CharField(max_length=3)
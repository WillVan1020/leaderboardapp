from pyexpat import model
from django.db import models

# Create your models here.
class results(models.Model):
    rank = models.TextField(max_length=20)
    name = models.TextField(max_length=50)
    points = models.IntegerField(max_length=20)

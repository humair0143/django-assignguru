from django.db import models

from django.urls import reverse

# Create your models here.

class Set(models.Model):
    setName = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
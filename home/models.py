from django.db import models

from django.urls import reverse

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Set(models.Model):
    name = models.CharField(max_length=2000)
    subjectName = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    setName = models.ForeignKey(Set, on_delete=models.CASCADE)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)

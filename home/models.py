from django.db import models

from django.urls import reverse

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=2000)

    def get_absolute_url(self):
        return reverse('sets', args=[str(self.id)])

class Set(models.Model):
    name = models.CharField(max_length=2000)
    subjectName = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('questions', args=[str(self.id)])

class Question(models.Model):
    setName = models.ForeignKey(Set, on_delete=models.CASCADE)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
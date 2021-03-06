from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
#from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, default=0)
    def __str__(self):
        return str(self.id) # return unique id of the object

class Schedule(models.Model):
    student = models.ForeignKey(Student, related_name='schedule', on_delete=models.CASCADE)
    # day 1 class holders
    d1p1 = models.CharField(max_length=150)
    d1p2 = models.CharField(max_length=150)
    d1p3 = models.CharField(max_length=150)
    d1p4 = models.CharField(max_length=150)
    # day 2 class holders
    d2p1 = models.CharField(max_length=150)
    d2p2 = models.CharField(max_length=150)
    d2p3 = models.CharField(max_length=150)
    d2p4 = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)

class Parent(models.Model):
    user = models.ForeignKey(User, related_name='parent', on_delete=models.CASCADE)
    kid1 = models.ForeignKey(Student, related_name='kid1', on_delete=models.CASCADE, null=True)
    kid2 = models.ForeignKey(Student, related_name='kid2', on_delete=models.CASCADE, null=True)
    kid3 = models.ForeignKey(Student, related_name='kid3', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)
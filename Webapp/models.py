from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student_Data(models.Model):
    sid = models.CharField(max_length=20,null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    semester = models.CharField(max_length=15, null=True, blank=True)
    branch = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.id)
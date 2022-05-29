from statistics import mode

from django.db import models
from django.forms import BooleanField

from users.models import User


class Project(models.Model):
    nameProject = models.CharField(max_length=64)
    linkProject = models.CharField(max_length=64)
    userSet = models.ManyToManyField(User)

    def __str__(self):
        return self.nameProject


class TODO(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    dateCreate = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    action = BooleanField(required=False)

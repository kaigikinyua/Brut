from django.db import models

# Create your models here.
class SuperUser(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    token=models.CharField(max_length=50)

class Action(models.Moldel):
    token=models.CharField(max_length=50)
    action=models.CharField(max_length=50)
    dot=models.DateTimeField(auto_now=False, auto_now_add=False)
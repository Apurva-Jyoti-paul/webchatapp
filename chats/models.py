from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class wpgc(models.Model):
    name=models.TextField(max_length=100,default='New_group')    ###group chat model
    members=models.ManyToManyField(User)
    creatorid=models.IntegerField(default=1)



class gchat(models.Model):
    chattxt=models.CharField(max_length=1000)
    writer=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    time=models.DateTimeField(default=timezone.now)
    groups=models.ForeignKey(wpgc,on_delete=models.CASCADE)

class profile(models.Model):
    status=models.TextField(max_length=1000)
    phn=models.TextField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
# Create your models here.

#developmental feature


from django.db import models

class UserGroup(models.Model):
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)
    ug = models.ForeignKey('UserGroup',null=True,on_delete=models.CASCADE)



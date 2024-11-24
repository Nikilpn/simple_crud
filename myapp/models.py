from django.db import models

# # Create your models here.
class StudentDb(models.Model):
    NAME=models.CharField(max_length=100,null=True,blank=True)
    AGE=models.IntegerField(null=True,blank=True)
    GENDER=models.CharField(max_length=100,null=True,blank=True)
    MOBILE=models.CharField(max_length=200,null=True,blank=True)
    TUTOR=models.CharField(max_length=120,null=True,blank=True)


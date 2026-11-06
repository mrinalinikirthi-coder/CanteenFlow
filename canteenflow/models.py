from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sno = models.CharField(max_length=100,unique = True)
    rollno = models.CharField(max_length = 25 , unique = True)
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 10)
    year = models.CharField(max_length = 10)
    section = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 10)
class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sno = models.CharField(max_length=100,unique = True)
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    role = models.CharField(max_length = 100)
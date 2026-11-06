from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.IntegerField(max_length=100,null = False,unique = True)
    rollno = models.IntegerField(max_length = 25 , null = False, unique = True)
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 10 , null = False)
    year = models.IntegerField(max_length = 10 , null = False)
    section = models.CharField(max_length = 10 , null = False)
    phone = models.IntegerField(max_length = 10 , null = False)
class Staff(models.Model):

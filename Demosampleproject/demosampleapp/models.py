from pyexpat import model
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_department = models.CharField(max_length=200)
    employee_phonenumber = models.IntegerField()
    employee_office_branch = models.CharField(max_length=200)
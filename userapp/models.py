from django.db import models

# Create your models here.

class temptb(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    temp_id=models.AutoField(primary_key=True)

class festtb(models.Model):
    name=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    fest_id=models.AutoField(primary_key=True)

class vazhitb(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    vazhi_id=models.AutoField(primary_key=True)
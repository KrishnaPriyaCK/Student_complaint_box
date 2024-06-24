from django.db import models

class register(models.Model):
    userphoto=models.CharField(max_length=200)
    useremail=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    userphone=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
class complaint(models.Model):
    userid=models.CharField(max_length=4)
    complaintto=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    complaintmesg=models.CharField(max_length=800)
    status=models.CharField(max_length=200)
class faculty(models.Model):
    designation=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
class acknowledgement(models.Model):
    name=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    ackmesg=models.CharField(max_length=800)
class facack(models.Model):
    date=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    ackmesg=models.CharField(max_length=800)








from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    skills=models.TextField(max_length=1000)
    about_you=models.TextField(max_length=1000)
    experience=models.TextField(max_length=1000)


class SignIn(models.Model):
    name1=models.CharField(max_length=100)
    mail=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)


class LogIn(models.Model):
    user_mail=models.CharField(max_length=100)
    user_password=models.CharField(max_length=50)
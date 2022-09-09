# from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class happy(models.Model):
    your_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    image=models.ImageField(upload_to='appkiimage')
    # Timestamp=models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.your_name
class sad(models.Model):
    your_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    image=models.ImageField(upload_to='appkiimage')
    # Timestamp=models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.your_name

class Complaints(models.Model):
   name = models.CharField(max_length=30)
   title = models.CharField(max_length=100)
   age = models.CharField(max_length=100, null=True, blank= True)
   gender = models.CharField(max_length=10)
   discription= models.TextField()
   image= models.ImageField(upload_to='appkiimage')

   def __str__(self):
       return self.name

class admlogin(models.Model):
   username = models.CharField(max_length=30)
   password = models.CharField(max_length=100)
   
   

   def __str__(self):
       return self.name 

class dash(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile= models.CharField(max_length=20)
    otp= models.CharField(max_length=8)

    def __str__(self):
       return self.user




from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class profile_Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    

class Profile(models.Model):
    #user = models.ForeignKey(User,on_delete=
    #models.SET_NULL,null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    objects = profile_Manager()
    admin_objects = models.Manager()


    def __str__(self):
        return self.first_name 
    
class CustomUser(AbstractBaseUser):
   email = models.EmailField(unique=True)
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
   gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
   contact = models.IntegerField(unique=True)

   USERNAME_FIELD = 'email'  
   REQUIRED_FIELDS = ['email','first_name','last_name','gender','contact'] 



   def __str__(self):
       return self.first_name


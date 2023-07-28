from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=
    models.SET_NULL,null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name 



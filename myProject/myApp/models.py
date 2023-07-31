from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.
class profile_Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=
    models.SET_NULL,null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    objects = profile_Manager()
    admin_objects = models.Manager()


    def __str__(self):
        return self.first_name 



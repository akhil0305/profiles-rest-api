from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)       #by default all users are active
    is_staff = models.BooleanField(default=False)       #by default all users are not staff and it should be set True only for staffs

    #Create Model Manager to use with Django Seelye. Model manager is created so that Django knows how to create and manage users.
    objects = UserProfileManager()

     USERNAME_FIELD = 'email'       #overwriting the default username field and replacing with the email. Since username field is set to email, it
                                    #means that email is required field.
     REQUIRED_FIELDS = ['name']     #specifying other required fields.

     """Adding functions that are used by Django to interact with our custom user model"""
     def get_full_name(self):
         """Retrieve fullname of user"""
         return self.name

     def  get_short_name(self):
         """Retrieve Short name of user"""
         return self.name

     def __str__(self):
         """Returns the value when you convert a UserProfile object to a string"""
         return self.email      #An object of UserProfile, that is, any user is identified by their email address.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime

# OPERATORS =( 
#     ("050", "050"), 
#     ("051", "051"), 
#     ("055", "055"), 
#     ("070", "070"), 
#     ("077", "077"),
#     ("099", "099"),
# )
class CustomUser(AbstractUser):
    # operators= models.CharField(max_length=3, choices=OPERATORS, null=True, blank=True)
    mobile = models.CharField(unique=True,max_length=10, null=True, blank=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta: 
        # ordering = ('-created_at',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    

class CustomUserRegistration(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)   
    shop_name = models.CharField(max_length=255, blank=False, null=False) 
    shop_link = models.URLField(max_length=255, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta: 
        # ordering = ('-created_at',)
        verbose_name = 'User (for selling)'
        verbose_name_plural = 'Users (for selling)'
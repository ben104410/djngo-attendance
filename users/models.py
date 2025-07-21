from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USER_TYPE_CHOICES = (
        ('staff', 'Staff'),
        ('community', 'Community Member'),
        ('admin', 'Administrator'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

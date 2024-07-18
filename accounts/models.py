from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Adding a customer field to the user model
    name = models.CharField(null=True, blank=True, max_length=100)



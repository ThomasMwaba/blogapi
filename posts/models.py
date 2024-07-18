from django.db import models

from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # Link to customuser
    created_at = models.DateField(auto_now_add=True) # Automatically set the date when it was created
    updated_date = models.DateField(auto_now=True) # Automatically set the date when it was updated
    
    def __str__(self):
        
        return self.title # The object is displayed as a string in the database
    
    

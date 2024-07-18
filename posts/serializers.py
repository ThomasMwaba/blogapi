from rest_framework import serializers

from django.contrib.auth import get_user_model

from . models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ("id",
                  "author",
                  "title",
                  "body",
                  "created_at",
        ) # fields to be serialized
        
        model = Post # uses Post model 
        
        


class UserSerializer(serializers.ModelSerializer):
        
        
    class Meta:
            
        model = get_user_model()  # uses customuser model 
            
        fields = ("id", "username") # fields to be serialized
        
        
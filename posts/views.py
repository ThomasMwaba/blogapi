from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer 

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """contains both the post-list and post detail views"""
    
    permission_classes = (IsAuthorOrReadOnly,) # The author of the post is the only one permitted to do all the methods
    
    queryset = Post.objects.all()
    # Gets all the instances of the post model 
    
    serializer_class = PostSerializer
    # uses the post serializer class 
    
    
    
class UserViewSet(viewsets.ModelViewSet):
    """contains both the user-list and user-detail views"""
    permission_classes = [IsAdminUser]
    # only the admin can view other users
    
    queryset = get_user_model().objects.all()
    # Gets all the instances of the post model 
    
    serializer_class = UserSerializer
    # uses the user serializer class 
    
    
    





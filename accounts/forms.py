from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
# forms to create new users   
    
    class Meta(UserCreationForm):
        
        model = CustomUser # uses custom model
        
        fields = UserCreationForm.Meta.fields + ("name",) # fields to be added
        
class CustomUserChangeForm(UserChangeForm):
# forms to change present users 
    
    class Meta:
        model = CustomUser # uses custom model
        
        fields = UserChangeForm.Meta.fields # fields to be added
        
        
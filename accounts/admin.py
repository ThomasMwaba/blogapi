from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    
    # The forms to add and change user instances
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    model = CustomUser
    
    # The fields to be used when showing the User model.
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),) # Personal information 
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),) # fields for the add form

    
    search_fields = ("username",) # fields to search in the admin
    
    
admin.site.register(CustomUser,CustomUserAdmin)
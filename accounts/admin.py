from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import CustomUser


from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "first_name", "last_name"]


admin.site.register(CustomUser, CustomUserAdmin)

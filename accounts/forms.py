from turtle import settiltangle
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")

    # def save(self, request):
    #     user = super(CustomUserCreationForm, self).save(request)

    #     user.username = self.cleaned_data["email"]
    #     user.save()

    #     return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")

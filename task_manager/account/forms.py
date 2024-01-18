from django import forms
from django.contrib.auth import get_user_model

from account.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data.get("password", "")

        if len(password) > 0:
            user.set_password(password)
        user.save()
        
        return user


# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from account.models import User


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("email",)


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ("email",)
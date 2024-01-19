from django import forms

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

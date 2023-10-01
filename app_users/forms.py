from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


from .models import CustomUser, AllowedUser


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser


class AllowedUserForm(forms.ModelForm):
    class Meta:
        model = AllowedUser
        fields = ('email',)
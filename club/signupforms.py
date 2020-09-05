from django import forms
from .models import UserStaffs, UserMembers
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupAdminForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email']


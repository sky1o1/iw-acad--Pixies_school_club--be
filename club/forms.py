from django import forms
from .models import UserStaffs, UserMembers, UserDetail
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['dob', 'address', 'phone_num', 'bio', 'profile_pic']
        read_only = ['id']
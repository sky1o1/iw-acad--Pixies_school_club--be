from django import forms
from .models import UserStaffs, UserMembers, UserDetail
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupAdminForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email']

    # def clean(self):
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data['confirm_password']
    #     if password != confirm_password:
    #         raise forms.ValidationError("Your passwords do not match")
    #
    #     if User.objects.filter(username=self.cleaned_data['username']).exists():
    #         raise forms.ValidationError('Username already taken')
    #     return self.cleaned_data['username']


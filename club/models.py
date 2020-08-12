from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    groups = None
    user_permissions = None


class UserStaffs(AbstractUser):
    middle_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)

    groups = None
    user_permissions = None


class UserMembers(AbstractUser):
    middle_name = models.CharField(max_length=50)

    groups = None
    user_permissions = None


class UserDetail(models.Model):
    dob = models.DateField()
    address = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='media/images/profile_pic')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_staffs = models.OneToOneField(UserStaffs, on_delete=models.CASCADE)
    user_members = models.OneToOneField(UserMembers, on_delete=models.CASCADE)


class Club(models.Model):
    president_name = models.CharField(max_length=150, default='Megha')
    club_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='media/images/club_pic/logo')

    def __str__(self):
        return self.club_name
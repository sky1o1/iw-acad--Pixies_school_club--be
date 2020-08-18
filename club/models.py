from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    groups = None
    user_permissions = None


class UserStaffs(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=True)

    groups = None
    user_permissions = None


class UserMembers(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)

    groups = None
    user_permissions = None


class UserDetail(models.Model):
    dob = models.DateField(default="2020-01-01")
    address = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile_pic')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_staffs = models.OneToOneField(UserStaffs, on_delete=models.CASCADE)
    user_members = models.OneToOneField(UserMembers, on_delete=models.CASCADE)


class Club(models.Model):
    president_name = models.CharField(max_length=150, default='Megha')
    club_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='images/club_pic/logo')
    created_by = models.CharField(max_length=200, default='Coder')
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_staffs = models.OneToOneField(UserStaffs, on_delete=models.CASCADE)
    user_members = models.ManyToManyField(UserMembers)

    def __str__(self):
        return self.club_name


class ContactPresident(models.Model):
    club_name = models.CharField(max_length=200)
    member_name = models.CharField(max_length=200)
    message_title = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)
    club = models.ForeignKey(UserStaffs, on_delete=models.CASCADE)
    member = models.ForeignKey(UserMembers, on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField(max_length=1000)
    event_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(UserStaffs, on_delete=models.CASCADE)
    club_event = models.ForeignKey(Club, on_delete=models.CASCADE)
    interested_members = models.ManyToManyField(UserMembers)
    all = models.BooleanField(default=False)


class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_description = models.TextField(max_length=1000)
    news_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(UserStaffs, on_delete=models.CASCADE)
    club_news = models.ForeignKey(Club, on_delete=models.CASCADE)
    all = models.BooleanField(default=False)


class Application(models.Model):
    members = models.ManyToManyField(UserMembers)
    interested_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


class Gallery(models.Model):
    images = models.ImageField(upload_to='images/club_pic/gallery')
    club_img = models.ManyToManyField(Club)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

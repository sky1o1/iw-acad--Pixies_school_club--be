from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Club(models.Model):
    club_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='images/club_pic/logo')


    def __str__(self):
        return self.club_name


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField('member status',default=True)

    groups = None
    user_permissions = None


class UserAdmin(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        groups = None
        user_permissions = None


class UserStaffs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    club_name = models.OneToOneField(Club, on_delete=models.CASCADE)


    groups = None
    user_permissions = None


class UserMembers(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    # club_name = models.ManyToManyField(Club)
    club_name = models.OneToOneField(Club, on_delete=models.CASCADE)
    groups = None
    user_permissions = None

class MemberApplicationRecord(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    club_name = models.CharField(max_length=200)
    email = models.EmailField()


class UserStaffDetail(models.Model):
    dob = models.DateField(default="2020-01-01")
    address = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile_pic')
    user_staff = models.OneToOneField(User, on_delete=models.CASCADE)

class UserMemberDetail(models.Model):
    dob = models.DateField(default="2020-01-01")
    address = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile_pic')
    user_member = models.OneToOneField(User, on_delete=models.CASCADE)

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
    event_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=150)
    created_by = models.ForeignKey(UserStaffs, on_delete=models.CASCADE, default=1)
    # club_event = models.ForeignKey(Club, on_delete=models.CASCADE, default=1)
    # interested_members = models.ManyToManyField(UserMembers)
    all = models.BooleanField(default=False)


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_description = models.TextField(max_length=1000)
    # news_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    created_by_staff = models.ForeignKey(UserStaffs, on_delete=models.CASCADE, blank=True, null=True)
    created_by_member = models.ForeignKey(UserMembers, on_delete=models.CASCADE, blank=True, null=True)
    # club_news = models.ForeignKey(Club, on_delete=models.CASCADE)
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

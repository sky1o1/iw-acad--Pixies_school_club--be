from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Club(models.Model):
    club_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='images/club_pic/logo', default='images/club_pic/logo/art.png')


    def __str__(self):
        return self.club_name


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField('member status',default=True)
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username


class UserAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    groups = None
    user_permissions = None


class UserStaffs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    club_name = models.OneToOneField(Club, on_delete=models.CASCADE)
    groups = None
    user_permissions = None
    def __str__(self):
        return self.user.username




class UserMembers(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE)
    groups = None
    user_permissions = None
    def __str__(self):
        return self.user.username



class MemberApplicationRecord(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    club_name = models.CharField(max_length=200)
    resume = models.ImageField(upload_to='images/resume',  null=True, blank=True)
    email = models.EmailField()


class ContactPresident(models.Model):
    message_title = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)
    club = models.CharField(max_length=200)
    # username = models.ForeignKey(UserMembers, on_delete=models.CASCADE)

    def __str__(self):
        return self.message_title


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField(max_length=1000)
    event_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    # created_by = models.CharField(max_length=150)
    # created_by = models.ForeignKey(UserStaffs, on_delete=models.CASCADE, default=1)
    all = models.BooleanField(default=False)


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_description = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    # created_by_staff = models.ForeignKey(UserStaffs, on_delete=models.CASCADE, blank=True, null=True)
    # created_by_member = models.ForeignKey(UserMembers, on_delete=models.CASCADE, blank=True, null=True)
    all = models.BooleanField(default=False)



class Gallery(models.Model):
    image = models.ImageField(upload_to='images/club_pic/gallery')
    # image2 = models.ImageField(upload_to='images/club_pic/gallery', blank=True, null=True)
    # image3 = models.ImageField(upload_to='images/club_pic/gallery', blank=True, null=True)

    # club_img = models.OneToOneField(Club)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

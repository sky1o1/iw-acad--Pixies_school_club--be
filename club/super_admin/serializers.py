from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Club, UserStaffs, UserMembers
User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'is_staff','is_member', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            middle_name=self.validated_data['middle_name'],
            username=self.validated_data['username'],
            is_staff=self.validated_data['is_staff'],
            is_member=self.validated_data['is_member'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],

        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class CreateClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['club_name', 'description', 'logo']

    def create(self, validated_data):
        club = Club(
            # president_name=self.validated_data['president_name'],
            club_name=self.validated_data['club_name'],
            description=self.validated_data['description'],
            logo=self.validated_data['logo'],
        )
        club.save()
        return club

class CreateUserStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStaffs
        fields = ['club_name', 'user']


    def create(self, validated_data):
        userstaffs = UserStaffs(
            # first_name=self.validated_data['first_name'],
            # last_name=self.validated_data['last_name'],
            # middle_name=self.validated_data['middle_name'],
            user=self.validated_data['user'],
            club_name=self.validated_data['club_name'],
            # email=self.validated_data['email'],
            # password=self.validated_data['password'],

        )
        # password = self.validated_data['password']
        # userstaffs.set_password(password)
        userstaffs.save()
        return userstaffs

class CreateUserMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembers
        fields = ['club_name', 'user']


    def create(self, validated_data):
        usermember = UserMembers(
            # first_name=self.validated_data['first_name'],
            # last_name=self.validated_data['last_name'],
            # middle_name=self.validated_data['middle_name'],
            user=self.validated_data['user'],
            club_name=self.validated_data['club_name'],
            # email=self.validated_data['email'],
            # password=self.validated_data['password'],

        )
        # password = self.validated_data['password']
        # userstaffs.set_password(password)
        usermember.save()
        return usermember



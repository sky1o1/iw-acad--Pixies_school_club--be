from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Club, UserStaffs

User = get_user_model()


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
        fields = ['first_name', 'last_name', 'middle_name', 'club_name', 'username', 'email', 'password']

    def create(self, validated_data):
        userstaffs = UserStaffs(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            middle_name=self.validated_data['middle_name'],
            username=self.validated_data['username'],
            club_name=self.validated_data['club_name'],

            email=self.validated_data['email'],
            password=self.validated_data['password'],

        )
        userstaffs.save()
        return userstaffs
from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Club, UserStaffs, UserMembers, ContactPresident
User = get_user_model()

class ContactPresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPresident
        fields = ['username', 'message_title', 'message', 'club']

    def create(self, validated_data):
        user = ContactPresident(
            username=self.validated_data['username'],
            message_title=self.validated_data['message_title'],
            message=self.validated_data['message'],
            club=self.validated_data['club'],
        )
        user.save()
        return user
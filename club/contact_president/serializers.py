from rest_framework import serializers
from django.contrib.auth import get_user_model
from club.models import ContactPresident
User = get_user_model()


class ContactPresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPresident
        fields = ['message_title', 'message', 'club','sent_by']

    def create(self, validated_data):
        user = ContactPresident(
            message_title=self.validated_data['message_title'],
            message=self.validated_data['message'],
            club=self.validated_data['club'],
            sent_by=self.validated_data['sent_by'],
        )
        user.save()
        return user


class ViewContactPresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPresident
        fields = ['id', 'message_title', 'message', 'club', 'sent_by']

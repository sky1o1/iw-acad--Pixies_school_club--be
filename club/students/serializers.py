from rest_framework import serializers
from club.models import ContactPresident

class ContactPresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPresident
        fields = ['id','club_name','member_name','message_title','message']

        
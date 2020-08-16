from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Club

User = get_user_model()


class CreateClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['president_name', 'club_name', 'description', 'logo']

    def create(self, validated_data):
        club = Club(
            president_name=self.validated_data['president_name'],
            club_name=self.validated_data['club_name'],
            description=self.validated_data['description'],
            logo=self.validated_data['logo'],
        )
        club.save()
        return club
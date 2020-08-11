from rest_framework import serializers

from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['president_name', 'club_name', 'description']
        ready_only = ['id']


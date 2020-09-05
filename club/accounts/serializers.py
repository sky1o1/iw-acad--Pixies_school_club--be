from rest_framework import serializers
from django.contrib.auth import get_user_model
from club.models import MemberApplicationRecord

User = get_user_model()


class MemberApplicationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberApplicationRecord
        fields = ['name', 'interest_reason', 'email','club_name']

    def validate(self, attrs):
        email = MemberApplicationRecord.objects.filter(email=attrs['email'])
        if email.exists():
            raise serializers.ValidationError('Email already in use')
        return attrs

    def create(self, validated_data):
        user = MemberApplicationRecord(
            name=self.validated_data['name'],
            interest_reason =self.validated_data['interest_reason'],
            email=self.validated_data['email'],
            club_name=self.validated_data['club_name'],

        )

        user.save()
        return user


class ViewMemberApplicationSerializer(serializers.ModelSerializer):
    club_name = serializers.SerializerMethodField(source='get_club_name')

    class Meta:
        model = MemberApplicationRecord
        fields = ['id','name', 'interest_reason', 'email','club_name']

    def create(self, validated_data):
        user = MemberApplicationRecord(
            id=self.validated_data['id'],
            name=self.validated_data['name'],
            interest_reason=self.validated_data['interest_reason'],
            email=self.validated_data['email'],
            club_name=self.validated_data['club_name'],

            )
        user.save()
        return user

    def get_club_name(self, obj):
        return obj.club_name.club_name


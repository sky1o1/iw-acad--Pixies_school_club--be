from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q

from club.models import UserStaffs, UserMembers

User = get_user_model()


class AdminRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = User.objects.filter(email=attrs['email'])
        if email.exists():
            raise serializers.ValidationError('Email already in use')

        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'Password do not match'})
        return attrs

    def create(self, validated_data):
        user = User(
            first_name=self.validated_data['first_name'],
            middle_name=self.validated_data['middle_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class StaffRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = UserStaffs
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = UserStaffs.objects.filter(email=attrs['email'])
        if email.exists():
            raise serializers.ValidationError('Email already in use')

        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'Password do not match'})
        return attrs

    def create(self, validated_data):
        user = UserStaffs(
            first_name=self.validated_data['first_name'],
            middle_name=self.validated_data['middle_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class MemberRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = UserMembers
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = UserMembers.objects.filter(email=attrs['email'])
        if email.exists():
            raise serializers.ValidationError('Email already in use')

        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'Password do not match'})
        return attrs

    def create(self, validated_data):
        user = UserMembers(
            first_name=self.validated_data['first_name'],
            middle_name=self.validated_data['middle_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class StaffLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = UserStaffs
        fields = ['username', 'password', 'email', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise serializers.ValidationError({'error': 'Email or Username required'})
        user = UserStaffs.objects.filter(
                Q(username=username) |
                Q(email=email)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError({'error': 'Username/Email is not valid'})
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError({'error': 'Incorrect password'})
        data['token'] = 'TOKEN'
        return data


class MemberLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = UserMembers
        fields = ['username', 'password', 'email', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise serializers.ValidationError({'error': 'Email or Username required'})
        user = UserStaffs.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError({'error': 'Username/Email is not valid'})
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError({'error': 'Incorrect password'})
        data['token'] = 'TOKEN'
        return data
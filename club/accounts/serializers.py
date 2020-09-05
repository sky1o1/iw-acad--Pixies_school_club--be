from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from club.models import UserStaffs, UserMembers, MemberApplicationRecord, UserAdmin

User = get_user_model()


class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = [ 'user']

    def create(self, validated_data):
        useradmin = UserAdmin(
            # first_name=self.validated_data['first_name'],
            # last_name=self.validated_data['last_name'],
            # middle_name=self.validated_data['middle_name'],
            user=self.validated_data['user'],
            # club_name=self.validated_data['club_name'],
            # email=self.validated_data['email'],
            # password=self.validated_data['password'],

        )
        # password = self.validated_data['password']
        # userstaffs.set_password(password)
        useradmin.save()
        return useradmin


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


class StaffLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
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
        user = User.objects.filter(
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
        return data


class MemberLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise serializers.ValidationError({'error': 'Email or Username required'})
        user = User.objects.filter(
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
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'middle_name', 'last_name','date_joined', 'email']

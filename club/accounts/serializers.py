from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token
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

# class StaffRegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(max_length=128, write_only=True)
#
#     class Meta:
#         model = UserStaffs
#         fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def validate(self, attrs):
#         email = UserStaffs.objects.filter(email=attrs['email'])
#         if email.exists():
#             raise serializers.ValidationError('Email already in use')
#
#         password = attrs['password']
#         confirm_password = attrs['confirm_password']
#         if password != confirm_password:
#             raise serializers.ValidationError({'Password do not match'})
#         return attrs
#
#     def create(self, validated_data):
#         user = UserStaffs(
#             first_name=self.validated_data['first_name'],
#             middle_name=self.validated_data['middle_name'],
#             # club_name =self.validated_data['club_name'],
#
#             last_name=self.validated_data['last_name'],
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],
#         )
#         password = self.validated_data['password']
#         user.set_password(password)
#         user.save()
#         return user


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
        # password = self.validated_data['password']
        # user.set_password(password)
        user.save()
        return user


class ViewMemberApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberApplicationRecord
        fields = ['name', 'interest_reason', 'email','club_name']


class StaffLoginSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(allow_blank=True, read_only=True)
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
        # data['token'] = Token
        return data


class MemberLoginSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(allow_blank=True, read_only=True)
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
        # data['token'] = 'TOKEN'
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'middle_name', 'last_name','date_joined', 'email']

from rest_framework import serializers
from django.contrib.auth import get_user_model
from club.models import Club, UserStaffs, UserMembers, Gallery
User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            middle_name=self.validated_data['middle_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],

        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class ViewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'username', 'email', 'password', 'is_staff', 'is_member']


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'username', 'email', 'password', 'is_staff', 'is_member']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            id=self.validated_data['id'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            middle_name=self.validated_data['middle_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            is_staff=self.validated_data['is_staff'],
            is_member=self.validated_data['is_member'],

        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class AdminFlagset(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_staff', 'is_member', 'username']

    def create(self, validated_data):
        user = User(
            is_staff=self.validated_data['is_staff'],
            is_member=self.validated_data['is_member'],
            username=self.validated_data['username'],
            # club = self.validated_data['club'],

        )
        user.save()
        return user


class CreateClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['club_name', 'description', 'logo']

    def create(self, validated_data):
        club = Club(
            logo=self.validated_data['logo'],
            club_name=self.validated_data['club_name'],
            description=self.validated_data['description'],
        )
        club.save()
        return club


class ViewClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id','logo', 'club_name', 'description']


class DeleteClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'club_name']



class CreateUserStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStaffs
        fields = ['club_name', 'user']

    def create(self, validated_data):
        userstaffs = UserStaffs(
            user=self.validated_data['user'],
            club_name=self.validated_data['club_name'],

        )
        userstaffs.save()
        return userstaffs


class CreateUserMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembers
        fields = ['club_name', 'user']

    def create(self, validated_data):
        usermember = UserMembers(
            user=self.validated_data['user'],
            club_name=self.validated_data['club_name'],

        )
        usermember.save()
        return usermember


class UserStaffSerializer(serializers.ModelSerializer):
    club_name = serializers.SerializerMethodField(source='get_club_name')
    user = serializers.SerializerMethodField(source='get_user')

    class Meta:
        model = UserStaffs
        fields = ['club_name', 'user']

    def get_club_name(self, obj):
        return obj.club_name.club_name

    def get_user(self, obj):
        return obj.user.username


class UserMemberSerializer(serializers.ModelSerializer):
    club_name = serializers.SerializerMethodField(source='get_club_name')
    user = serializers.SerializerMethodField(source='get_user')

    class Meta:
        model = UserMembers
        fields = ['club_name', 'user']

    def get_club_name(self, obj):
        return obj.club_name.club_name

    def get_user(self, obj):
        return obj.user.username


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']

    def create(self, validated_data):
        gallery = Gallery(
            image=self.validated_data['image'],
        )
        gallery.save()
        return gallery


class ViewGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']

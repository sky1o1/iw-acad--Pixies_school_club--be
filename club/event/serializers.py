from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Event



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_title', 'event_description', 'event_date', 'all', 'created_by']

    def create(self, validated_data):
        user = Event(
            # president_name=self.validated_data['president_name'],
            event_title=self.validated_data['event_title'],
            event_description=self.validated_data['event_description'],
            event_date=self.validated_data['event_date'],
            created_by = self.validated_data['created_by'],
            # club_event =self.validated_data['club_event'],

            all=self.validated_data['all'],

        )

        user.save()
        return user

#
# class EventPost(serializers.ModelSerializer):
#     token = serializers.CharField(allow_blank=True, read_only=True)
#     event_title = serializers.CharField(required=False, allow_blank=True)
#     event_description = serializers.CharField(required=False, allow_blank=True)
#     event_date = serializers.DateField(required=False)
#     all=serializers.BooleanField()
#
#     class Meta:
#         model = Event
#         fields = ['event_title', 'event_description', 'event_date', 'all', 'token']
#
#     def validate(self, data):
#         user_obj = None
#         event_title = data.get('event_title', None)
#         event_description = data.get('username', None)
#         event_date = data.get('event_date',None)
#         all = data.get('all', None)
#
#         data['token'] = 'TOKEN'
#         return data



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
#             last_name=self.validated_data['last_name'],
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],
#         )
#         password = self.validated_data['password']
#         user.set_password(password)
#         user.save()
#         return user
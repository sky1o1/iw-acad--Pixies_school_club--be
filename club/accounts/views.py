from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import AdminRegistrationSerializer, MemberApplicationRecordSerializer, StaffLoginSerializer, MemberLoginSerializer
from club.models import UserStaffs, UserMembers, UserAdmin

User = get_user_model()


class AdminRegistrationView(ListCreateAPIView):
    queryset = UserAdmin.objects.all()
    serializer_class = AdminRegistrationSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        # data['email'] = account.email
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
        return Response(data,   status=status.HTTP_201_CREATED)


# class StaffRegistrationView(ListCreateAPIView):
#     queryset = UserStaffs.objects.all()
#     serializer_class = StaffRegistrationSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [AllowAny, ]
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         data = {}
#         serializer.is_valid(raise_exception=True)
#         account = serializer.save()
#         data['response'] = 'Successfully created a new user'
#         data['email'] = account.email
#         data['username'] = account.username
#         token = Token.objects.get(user=account).key
#         data['token'] = token
#         return Response(data, status=status.HTTP_201_CREATED)
#

class MemberApplicationRecordSerializerView(ListCreateAPIView):
    queryset = UserMembers.objects.all()

    serializer_class = MemberApplicationRecordSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data['response'] = 'Successfully created a new user'
        data['first_name'] = account.first_name
        data['last_name'] = account.last_name
        data['middle_name'] = account.middle_name
        data['club_name'] = account.club_name
        data['email'] = account.email
        token = Token.objects.get(user=account).key
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)


class StaffLoginView(APIView):
    serializer_class = StaffLoginSerializer
    queryset = UserStaffs.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        new_data = serializer.data
        return Response(new_data, status=status.HTTP_200_OK)


class MemberLoginView(APIView):
    serializer_class = MemberLoginSerializer
    queryset = UserMembers.objects.all()
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):

    def get(self, request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
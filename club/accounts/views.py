from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status, generics
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from club.permissions import IsStaffUser, IsSuperUser


from .serializers import AdminRegistrationSerializer, ProfileSerializer, MemberApplicationRecordSerializer, StaffLoginSerializer, MemberLoginSerializer
from club.models import  UserMembers, UserAdmin, MemberApplicationRecord

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
        data['token'] = token.key
        return Response(data,   status=status.HTTP_201_CREATED)




class MemberApplicationRecordSerializerView(ListCreateAPIView):
    queryset = MemberApplicationRecord.objects.all()

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
        return Response(data, status=status.HTTP_201_CREATED)

class MemberApplicationViewSerializerView(ListCreateAPIView):
    serializer_class = MemberApplicationRecordSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsStaffUser,IsStaffUser, ]
    def get_queryset(self):
        return MemberApplicationRecord.objects.all()

class LogoutView(APIView):

    def get(self, request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class ProfileAPI(RetrieveAPIView):

    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk= kwargs['id'])
        profile_serializer = ProfileSerializer(user)
        return Response(profile_serializer.data)
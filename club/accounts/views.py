from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status, generics
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from club.permissions import IsStaffUser, IsSuperUser


from .serializers import AdminRegistrationSerializer, ProfileSerializer, MemberApplicationRecordSerializer, StaffLoginSerializer, MemberLoginSerializer,ViewMemberApplicationSerializer
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
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully appointed as president'

        return Response(data, status=status.HTTP_201_CREATED)


class MemberApplicationViewSerializerView(ListAPIView):
    serializer_class = ViewMemberApplicationSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny,]
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
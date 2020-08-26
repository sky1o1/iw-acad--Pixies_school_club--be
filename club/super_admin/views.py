from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView,  CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import CreateClubSerializer, CreateUserStaffSerializer, CreateUserSerializer, CreateUserMemberSerializer
from club.models import Club, UserStaffs, UserMembers
from club.permissions import IsStaffUser, IsSuperUser
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
User = get_user_model()

#admin can create and view club
class AdminClubView(ListCreateAPIView):
    queryset = Club.objects.all()

    serializer_class = CreateClubSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuperUser, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully created Club'
        return Response(data, status=status.HTTP_201_CREATED)

#others can view the clubs created by admin
class ClubView(ListAPIView):

    serializer_class = CreateClubSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]
    def get_queryset(self):
        return Club.objects.all()


#admin creates and view staffs(presidents) of each club
class AdminUserStaffView(ListCreateAPIView):
    queryset = UserStaffs.objects.all()

    serializer_class = CreateUserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuperUser, ]


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully appointed as president'

        return Response(data, status=status.HTTP_201_CREATED)

#others can view the president
class UserStaffView(ListAPIView):
    queryset = UserStaffs.objects.all()

    serializer_class = CreateUserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

#selected president can add member to the club
class AddUserMemberView(ListCreateAPIView):
    queryset = UserMembers.objects.all()

    serializer_class = CreateUserMemberSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsStaffUser, ]


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        usermember = serializer.save()
        data['response'] = 'Succesfully created Club'
        token = Token.objects.get(user=usermember).key
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)

#admin can add users
class AdminUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuperUser, ]


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        User = serializer.save()
        data['response'] = 'Succesfully created user'
        return Response(data, status=status.HTTP_201_CREATED)

#authenticated user can view the list of entire user
class UserView(ListAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuperUser,IsStaffUser, ]
    search_backend = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['username']
    order_fields = ['id']
    filterset_fields =['username','id']

    def get_queryset(self):
        return User.objects.all()

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import CreateClubSerializer, CreateUserStaffSerializer
from club.models import Club, UserStaffs
from club.permissions import IsSuperUser

User = get_user_model()


class AdminClubView(ListCreateAPIView):
    queryset = Club.objects.all()

    serializer_class = CreateClubSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully created Club'
        token = Token.objects.get(user=club).key
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)


class AdminUserStaffView(ListCreateAPIView):
    queryset = UserStaffs.objects.all()

    serializer_class = CreateUserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    data = {}
    serializer.is_valid(raise_exception=True)
    club = serializer.save()
    data['response'] = 'Succesfully created Club'
    token = Token.objects.get(user=club).key
    data['token'] = token
    return Response(data, status=status.HTTP_201_CREATED)


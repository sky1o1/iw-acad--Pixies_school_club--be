from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateClubSerializer
from club.models import Club
from club.permissions import IsSuperUser

User = get_user_model()


class AdminClubViewSet(ModelViewSet):
    serializer_class = CreateClubSerializer
    queryset = Club.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuperUser, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

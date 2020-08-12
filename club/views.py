from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Club
from .serializers import ClubSerializer


class ClubViewSet(ViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()






from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import Club
from .serializers import ClubSerializer


class ClubViewSet(ViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()

    # def get(self, request, *args, **kwargs):
    #     qs = club.objects.all()
    #     serializer = clubserializer(instance=qs, many=true)
    #     return response(serializer.data)





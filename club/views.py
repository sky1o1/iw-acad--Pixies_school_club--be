from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Club
from .serializers import ClubSerializer


class ClubView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Club.objects.all()
        serializer = ClubSerializer(instance=qs, many=True)
        return Response(serializer.data)





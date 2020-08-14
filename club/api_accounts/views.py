from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView

from .serializers import AdminRegistrationSerializer, StaffRegistrationSerializer, MemberRegistrationSerializer

User = get_user_model()


class AdminRegistrationView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = AdminRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#
# @api_view(['POST', ])
# def signup_view(request):
#     if request.method == 'POST':
#         serializer = LoginAdminSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             data = serializer.errors
#         return Response(data)


class StaffRegistrationView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = StaffRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MemberRegistrationView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = MemberRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
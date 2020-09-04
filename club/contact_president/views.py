from django.contrib.auth import authenticate, login, get_user_model, logout

from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView,  CreateAPIView,UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import ContactPresidentSerializer, ViewContactPresidentSerializer
from club.models import Club, UserStaffs, UserMembers, ContactPresident
from club.permissions import IsStaffUser, IsSuperUser
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

User = get_user_model()

#admin can create and view club


class ContactPresidentView(CreateAPIView):
    queryset = ContactPresident.objects.all()

    serializer_class = ContactPresidentSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully sent message'
        return Response(data, status=status.HTTP_201_CREATED)


class ContactPresidentMessageView(ListAPIView):
    queryset = ContactPresident.objects.all()

    serializer_class = ViewContactPresidentSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

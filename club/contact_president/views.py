from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListAPIView,  CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import ContactPresidentSerializer, ViewContactPresidentSerializer
from club.models import ContactPresident
from club.permissions import IsStaffUser, IsMember
from rest_framework.permissions import AllowAny
User = get_user_model()


class ContactPresidentView(CreateAPIView):
    queryset = ContactPresident.objects.all()
    serializer_class = ContactPresidentSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully sent message'
        return Response(data, status=status.HTTP_201_CREATED)


class ContactPresidentMessageView(ListAPIView):
    queryset = ContactPresident.objects.all()

    serializer_class = ViewContactPresidentSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

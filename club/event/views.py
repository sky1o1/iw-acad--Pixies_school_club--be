from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import EventSerializer
from club.models import UserStaffs, UserMembers, Club, Event

User = get_user_model()
class EventSerializerView(CreateAPIView):
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        data['response'] = 'Successfully Posted'
        data['event_title'] = event.event_title
        data['event_description'] = event.event_description
        data['event_date'] = event.event_date
        data['all'] = event.all
        # token = Token.objects.get(user=event).key
        # data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)





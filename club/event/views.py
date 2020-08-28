from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from club.permissions import IsStaffUser, IsSuperUser

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import EventSerializer
from club.models import Event
from django.shortcuts import get_object_or_404

User = get_user_model()
class EventSerializerView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsStaffUser,IsSuperUser, ]

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

        return Response(data, status=status.HTTP_201_CREATED)


class EventView(RetrieveAPIView):
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['id'])
        event_serializer = EventSerializer(user)
        return Response(event_serializer.data)






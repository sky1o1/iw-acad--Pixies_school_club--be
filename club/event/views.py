from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from club.permissions import IsStaffUser, IsSuperUser
from rest_framework.response import Response
from .serializers import EventSerializer,ViewEventSerializer
from club.models import Event
from rest_framework.permissions import AllowAny


User = get_user_model()


class EventSerializerView(CreateAPIView):
    queryset = Event.objects.all()
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
        data['created_by'] = event.created_by

        return Response(data, status=status.HTTP_201_CREATED)


class EventView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ViewEventSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]







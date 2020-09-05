from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from club.permissions import IsStaffUser
from .serializers import MemberApplicationRecordSerializer, ViewMemberApplicationSerializer
from club.models import MemberApplicationRecord

User = get_user_model()


class MemberApplicationRecordSerializerView(ListCreateAPIView):
    queryset = MemberApplicationRecord.objects.all()
    serializer_class = MemberApplicationRecordSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully sent the application'
        return Response(data, status=status.HTTP_201_CREATED)


class MemberApplicationSerializerView(ListAPIView):
    serializer_class = ViewMemberApplicationSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return MemberApplicationRecord.objects.all()


class DeleteMemberApplication(ModelViewSet):
    queryset = MemberApplicationRecord.objects.all()
    serializer_class = ViewMemberApplicationSerializer
    permission_classes = [AllowAny, ]


class LogoutView(APIView):

    def get(self, request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


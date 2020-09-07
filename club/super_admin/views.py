from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView,  CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateClubSerializer, CreateUserStaffSerializer, UpdateUserSerializer, AdminFlagset, \
    ViewClubSerializer, ViewUserSerializer,  CreateUserSerializer, CreateUserMemberSerializer, GallerySerializer,\
    ViewGallerySerializer, UserStaffSerializer, UserMemberSerializer, DeleteClubSerializer
from club.models import Club, UserStaffs, UserMembers, Gallery
from club.permissions import IsStaffUser, IsSuperUser,IsMember
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

User = get_user_model()


class AdminClubView(CreateAPIView):
    queryset = Club.objects.all()

    serializer_class = CreateClubSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully created Club'
        return Response(data, status=status.HTTP_201_CREATED)


class ClubView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ViewClubSerializer
    permission_classes = [AllowAny, ]


class DeleteClub(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = DeleteClubSerializer
    permission_classes = [AllowAny, ]


class AdminUserStaffView(ListCreateAPIView):
    queryset = UserStaffs.objects.all()
    serializer_class = CreateUserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully appointed as president'
        return Response(data, status=status.HTTP_201_CREATED)


class UserStaffView(ListAPIView):
    queryset = UserStaffs.objects.all()
    serializer_class = UserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


class AddUserMemberView(ListCreateAPIView):
    queryset = UserMembers.objects.all()
    serializer_class = CreateUserMemberSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully Added Member'
        return Response(data, status=status.HTTP_201_CREATED)


class UserMemberView(ListAPIView):
    queryset = UserMembers.objects.all()
    serializer_class = UserMemberSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


class SignupUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully created user'
        return Response(data, status=status.HTTP_201_CREATED)


class UpdateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [AllowAny, ]


class AdminFlagsetview(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminFlagset
    permission_classes = [AllowAny, ]


class UserView(ListAPIView):
    serializer_class = ViewUserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]
    search_backend = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['username']
    order_fields = ['id']
    filter_set_fields = ['username', 'id']

    def get_queryset(self):
        return User.objects.all()


class CreateGalleryView(ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'Successfully uploaded pictures to Gallery'
        return Response(data, status=status.HTTP_201_CREATED)


class GalleryView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = ViewGallerySerializer
    permission_classes = [AllowAny, ]


class SinglePictureView(RetrieveAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Gallery, pk= kwargs['id'])
        profile_serializer = GallerySerializer(user)
        return Response(profile_serializer.data)
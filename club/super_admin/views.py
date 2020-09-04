from django.contrib.auth import authenticate, login, get_user_model, logout

from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView,  CreateAPIView,UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateClubSerializer, CreateUserStaffSerializer, UpdateUserSerializer,AdminFlagset,ViewClubSerializer  , ViewUserSerializer,  CreateUserSerializer, CreateUserMemberSerializer, GallerySerializer, ViewGallerySerializer, UserStaffSerializer, UserMemberSerializer
from club.models import Club, UserStaffs, UserMembers, Gallery
from club.permissions import IsStaffUser, IsSuperUser
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

User = get_user_model()

#admin can create and view club
class AdminClubView(CreateAPIView):
    queryset = Club.objects.all()

    serializer_class = CreateClubSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully created Club'
        return Response(data, status=status.HTTP_201_CREATED)

#others can view the clubs created by admin
class ClubView(ListAPIView):
    queryset = Club.objects.all()

    serializer_class = ViewClubSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]
    def get_queryset(self):
        return Club.objects.all()


#admin creates and view staffs(presidents) of each club
class AdminUserStaffView(ListCreateAPIView):
    queryset = UserStaffs.objects.all()

    serializer_class = CreateUserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        club = serializer.save()
        data['response'] = 'Succesfully appointed as president'

        return Response(data, status=status.HTTP_201_CREATED)

#others can view the president
class UserStaffView(ListAPIView):
    queryset = UserStaffs.objects.all()

    serializer_class = UserStaffSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

#selected president can add member to the club
class AddUserMemberView(ListCreateAPIView):
    queryset = UserMembers.objects.all()

    serializer_class = CreateUserMemberSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        usermember = serializer.save()
        data['response'] = 'Succesfully Added Member'
        return Response(data, status=status.HTTP_201_CREATED)


class UserMemberView(ListAPIView):
    queryset = UserMembers.objects.all()

    serializer_class = UserMemberSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

#admin can add users
class SignupUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        User = serializer.save()
        data['response'] = 'Succesfully created user'
        return Response(data, status=status.HTTP_201_CREATED)


#for delete and update
class UpdateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [AllowAny, ]


#for admin(can set flag for users)
class AdminFlagsetview(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminFlagset
    permission_classes = [AllowAny,]


     #authenticated user can view the list of entire user
class UserView(ListAPIView):
    serializer_class = ViewUserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny ]
    search_backend = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['username']
    order_fields = ['id']
    filterset_fields =['username','id']

    def get_queryset(self):
        return User.objects.all()


class CreateGalleryView(ListCreateAPIView):
    queryset = Gallery.objects.all()

    serializer_class = GallerySerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        gallery = serializer.save()
        # data['image2']=gallery.image2
        # data['image3']=gallery.image3
        data['response'] = 'Succesfully uploaded pictures to Gallery'
        return Response(data, status=status.HTTP_201_CREATED)


class GalleryView(ListAPIView):
    queryset = Gallery.objects.all()

    serializer_class = ViewGallerySerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


class SinglePictureView(RetrieveAPIView):

    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Gallery, pk= kwargs['id'])
        profile_serializer = GallerySerializer(user)
        return Response(profile_serializer.data)
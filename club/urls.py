from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .event.views import  EventSerializerView, EventView
from .article.views import ArticleSerializerView, ArticleView
from club.super_admin.views import AdminClubView,SinglePictureView, UpdateUserView, AdminUserStaffView, AdminFlagsetview, \
    SignupUserView, AddUserMemberView, ClubView, UserStaffView, UserView, CreateGalleryView, GalleryView, UserMemberView, DeleteClub
from club.contact_president.views import ContactPresidentView, ContactPresidentMessageView
from .accounts.views import MemberApplicationRecordSerializerView, LogoutView, \
    MemberApplicationSerializerView, DeleteMemberApplication

r = DefaultRouter()
r.register('info/view-profile', UpdateUserView)
r.register('admin/set-flag', AdminFlagsetview)
r.register('delete-application', DeleteMemberApplication)
r.register('delete-club', DeleteClub)


urlpatterns = [
    #AllowAny
    path('view-club/', ClubView.as_view(), name='club'),
    path('view-staff/', UserStaffView.as_view(), name='staff'),
    path('gallery/', GalleryView.as_view()),

    #signup to be an user
    path('add-user/', SignupUserView.as_view(), name='add-user'),

    #Login
    path('login/', obtain_auth_token, name='login'),

    #Logged in user
    path('contact-president/', ContactPresidentView.as_view()),
    path('article/', ArticleView.as_view(), name='article'),
    path('event/', EventView.as_view(), name='event'),
    path('member-application/', MemberApplicationRecordSerializerView.as_view(), name='member-applicaion'),

    #Superuser or Admin
    path('add-club/', AdminClubView.as_view(), name='add-club'),  # add club by superadmin only
    path('view-members/', UserMemberView.as_view()),
    path('add-president/', AdminUserStaffView.as_view(), name='admin/add-president'),
    path('user-view/', UserView.as_view(), name='login/user-view'),
    path('post-article/', ArticleSerializerView.as_view()),

    #For President of Club
    path('view-application/', MemberApplicationSerializerView.as_view(), name= 'view-application'),
    path('add-member/', AddUserMemberView.as_view(), name='member-signup'),
    path('upload-gallery/', CreateGalleryView.as_view()),
    path('post-event/', EventSerializerView.as_view()),
    path('view-message/', ContactPresidentMessageView.as_view()),


    path('logout/', LogoutView.as_view(), name='logout'),
    path('<id>/', SinglePictureView.as_view()),
              ] + r.urls
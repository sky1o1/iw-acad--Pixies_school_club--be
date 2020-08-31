from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import home
from .event.views import  EventSerializerView, EventView
from .article.views import ArticleSerializerView, ArticleView
from club.super_admin.views import AdminClubView, UpdateUserView, AdminUserStaffView, AdminFlagsetview,  SignupUserView, AddUserMemberView, ClubView, UserStaffView, UserView, CreateGalleryView, GalleryView
from club.contact_president.views import ContactPresidentView, ContactPresidentMessageView
from .accounts.views import AdminRegistrationView, MemberApplicationRecordSerializerView, ProfileAPI, LogoutView, MemberApplicationViewSerializerView
r = DefaultRouter()
r.register('info/view-profile', UpdateUserView)
r.register('admin/set-flag', AdminFlagsetview)



urlpatterns = [
    path('', home, name='home'),
    path('view-club/', ClubView.as_view(), name='club'),
    path('view-staff/', UserStaffView.as_view(), name='staff'),
    path('member-application/', MemberApplicationRecordSerializerView.as_view(), name='member-applicaion'),
    path('login/', obtain_auth_token, name='login'),
    path('signup/admin/', AdminRegistrationView.as_view(), name='admin-signup'),
    path('add-user/', SignupUserView.as_view(), name='add-user'),
    path('add-club/', AdminClubView.as_view(), name='add-club'),
    path('view-application/', MemberApplicationViewSerializerView.as_view(), name= 'view-application'),
    path('add-president/', AdminUserStaffView.as_view(), name='admin/add-president'),
    path('add-member/', AddUserMemberView.as_view(), name='member-signup'),
    path('user-view/', UserView.as_view(), name='login/user-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('article/', ArticleView.as_view(), name= 'article'),
    path('event/', EventView.as_view(), name='event'),
    path('post-event/', EventSerializerView.as_view()),
    path('post-article/', ArticleSerializerView.as_view()),
    path('<id>/profile/', ProfileAPI.as_view()),
    path('upload-gallery/', CreateGalleryView.as_view()),
    path('gallery/', GalleryView.as_view()),
    path('contact-president/', ContactPresidentView.as_view()),
    path('view-message/', ContactPresidentMessageView.as_view()),

              ] + r.urls
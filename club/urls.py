from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import ClubViewSet, home
from .event.views import  EventSerializerView, EventView
from .article.views import ArticleSerializerView, ArticleView
from club.super_admin.views import AdminClubView, UpdateUserView, AdminUserStaffView, AdminFlagsetview,  SignupUserView, AddUserMemberView, ClubView, UserStaffView, UserView

from .accounts.views import AdminRegistrationView, MemberApplicationRecordSerializerView, ProfileAPI, LogoutView, MemberApplicationViewSerializerView
r = DefaultRouter()
r.register('info/view-profile', UpdateUserView)
r.register('admin/set-flag', AdminFlagsetview)


urlpatterns = [
    path('home/', home, name='home'),
    path('view-club/', ClubView.as_view(), name='club'),
    path('view-staff/', UserStaffView.as_view(), name='staff'),
    path('member-application/', MemberApplicationRecordSerializerView.as_view(), name='member-applicaion'),
    path('login/', obtain_auth_token, name='login'),
    path('signup/admin/', AdminRegistrationView.as_view(), name='admin-signup'),
    path('add-user/', SignupUserView.as_view(), name='add-user'),
    path('login/admin/add-club/', AdminClubView.as_view(), name='add-club'),
    path('login/view-application/', MemberApplicationViewSerializerView.as_view(), name= 'view-application'),
    path('login/admin/add-president/', AdminUserStaffView.as_view(), name='admin/add-president'),
    path('login/admin/add-member/', AddUserMemberView.as_view(), name='member-signup'),
    path('login/user-view/', UserView.as_view(), name='login/user-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<id>/article/', ArticleView.as_view(), name= 'article'),
    path('<id>/event/', EventView.as_view(), name='event'),
    path('login/post-event/', EventSerializerView.as_view()),
    path('login/post-article/', ArticleSerializerView.as_view()),
    path('login/<id>/profile/', ProfileAPI.as_view()),


              ] + r.urls
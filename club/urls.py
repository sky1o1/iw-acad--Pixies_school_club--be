from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import ClubViewSet, home
from .event.views import  EventSerializerView
from .article.views import ArticleSerializerView
from club.super_admin.views import AdminClubView, AdminUserStaffView, AdminUserView, AddUserMemberView, ClubView, UserStaffView, UserView

from .accounts.views import AdminRegistrationView, MemberApplicationRecordSerializerView, StaffLoginView, MemberLoginView, LogoutView
r = DefaultRouter()
# r.register('clubs,', ClubViewSet)


urlpatterns = [
    # path('clubs/', ClubViewSet.as_view,
    # path('signup/staff/', StaffRegistrationView.as_view()),
    path('home/', home, name='home'),
    path('login/', obtain_auth_token, name='login'),
    path('signup/admin/', AdminRegistrationView.as_view(), name='admin-signup'),
    path('login/admin/add-user/', AdminUserView.as_view(), name='add-user'),
    path('login/admin/add-club/', AdminClubView.as_view(), name='add-club'),
    path('login/admin/add-president/', AdminUserStaffView.as_view(), name='admin/add-president'),
    path('login/admin/add-member/', AddUserMemberView.as_view(), name='member-signup'),
    path('member-application/', MemberApplicationRecordSerializerView.as_view(), name= 'member-applicaion'),

    # path('login/staff/', StaffLoginView.as_view(), name='login/staff'),
    # path('login/member/', MemberLoginView.as_view(), name='login/member'),
    path('login/user-view/', UserView.as_view(), name='login/user-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('post/', EventPostView.as_view()),
    path('login/event/', EventSerializerView.as_view()),
    path('login/article/', ArticleSerializerView.as_view()),
    path('view-club/', ClubView.as_view(), name='club'),
    path('view-staff/', UserStaffView.as_view(), name='staff'),

] + r.urls
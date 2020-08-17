from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import ClubViewSet, home
from .accounts.views import AdminRegistrationView, StaffRegistrationView, MemberRegistrationView, StaffLoginView, MemberLoginView, LogoutView
r = DefaultRouter()
# r.register('clubs,', ClubViewSet)


urlpatterns = [
    # path('clubs/', ClubViewSet.as_view,
    path('signup/admin/', AdminRegistrationView.as_view()),
    path('signup/staff/', StaffRegistrationView.as_view()),
    path('signup/member/', MemberRegistrationView.as_view()),
    path('login/', obtain_auth_token, name='login'),
    path('login/staff/', StaffLoginView.as_view(), name='login/staff'),
    path('login/member/', MemberLoginView.as_view(), name='login/member'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),
] + r.urls
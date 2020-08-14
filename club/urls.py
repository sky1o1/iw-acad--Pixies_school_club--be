from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import ClubViewSet, LoginAdminViewSet, SignupAdminViewSet, home
from .api_accounts.views import AdminRegistrationView, StaffRegistrationView, MemberRegistrationView


r = DefaultRouter()
r.register('clubs,', ClubViewSet)


urlpatterns = [
    # path('clubs/', ClubViewSet.as_view,
    path('signup/admin/', AdminRegistrationView.as_view()),
    path('signup/staff/', StaffRegistrationView.as_view()),
    path('signup/member/', MemberRegistrationView.as_view()),
    path('home/', home),
    path('home/', home),
] + r.urls
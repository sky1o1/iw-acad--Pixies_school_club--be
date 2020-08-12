from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ClubViewSet, LoginAdminViewSet, SignupAdminViewSet, home


r = DefaultRouter()
r.register('clubs,', ClubViewSet)


urlpatterns = [
    # path('clubs/', ClubViewSet.as_view,
    path('login/admin/', LoginAdminViewSet.as_view()),
    path('signup/admin/', SignupAdminViewSet.as_view()),
    path('home/', home),
] + r.urls
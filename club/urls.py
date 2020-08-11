from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ClubViewSet


r = DefaultRouter()
r.register('clubs,', ClubViewSet)


urlpatterns = [
    # path('clubs/', ClubView.as_view())
] + r.urls
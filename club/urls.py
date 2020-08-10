from django.urls import path

from .views import ClubView

urlpatterns = [
    path('clubs/', ClubView.as_view())
]
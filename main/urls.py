"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token



from club.super_admin.views import AdminClubView, AdminUserStaffView, AdminUserView, AdminUserMemberView
from club.accounts.views import AdminRegistrationView
r = DefaultRouter()


urlpatterns = [
    path('signup/', obtain_auth_token),
    path('signup/admin/', AdminRegistrationView.as_view(), name='admin-signup'),
    path('signup/admin/add-member/', AdminUserMemberView.as_view(), name='member-signup'),
    path('signup/admin/add-user', AdminUserView.as_view(), name='add-user'),
    path('signup/admin/add-club/', AdminClubView.as_view(), name='add-club'),
    path('signup/admin/add-president/', AdminUserStaffView.as_view(), name='admin/add-president'),
    # path('signup/', include('django.contrib.auth.urls')),
    path('', include('club.urls')),
] + r.urls

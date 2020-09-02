from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import home
from .event.views import  EventSerializerView, EventView
from .article.views import ArticleSerializerView, ArticleView
from club.super_admin.views import AdminClubView,SinglePictureView, UpdateUserView, AdminUserStaffView, AdminFlagsetview,  SignupUserView, AddUserMemberView, ClubView, UserStaffView, UserView, CreateGalleryView, GalleryView
from club.contact_president.views import ContactPresidentView, ContactPresidentMessageView
from .accounts.views import AdminRegistrationView, MemberApplicationRecordSerializerView, ProfileAPI, LogoutView, MemberApplicationViewSerializerView
r = DefaultRouter()
r.register('info/view-profile', UpdateUserView) #user le afno profile update /delete garni
r.register('admin/set-flag', AdminFlagsetview)#admin le is_staff/is_member flag set garni (default member=true)



urlpatterns = [
    path('', home, name='home'),
    path('view-club/', ClubView.as_view(), name='club'), #list club view( Allowany)
    path('view-staff/', UserStaffView.as_view(), name='staff'), #view president( Allowany)
    path('member-application/', MemberApplicationRecordSerializerView.as_view(), name='member-applicaion'), #post member application (allow any)
    path('login/', obtain_auth_token, name='login'),#login for all
    path('signup/admin/', AdminRegistrationView.as_view(), name='admin-signup'), #not in use
    path('add-user/', SignupUserView.as_view(), name='add-user'), #signup ,anyone can signup
    path('add-club/', AdminClubView.as_view(), name='add-club'), #add club by superadmin only
    path('view-application/', MemberApplicationViewSerializerView.as_view(), name= 'view-application'), #view application by president and superadmin
    path('add-president/', AdminUserStaffView.as_view(), name='admin/add-president'), #add president by superadmin(kun club ko kun president assign garni matra
    path('add-member/', AddUserMemberView.as_view(), name='member-signup'), #add member by president kun club ko kun member matra(remember not flagset)(chuttai table ho)
    path('user-view/', UserView.as_view(), name='login/user-view'),#list of all the signed up  user( superuser and president can only view
    path('logout/', LogoutView.as_view(), name='logout'),
    path('article/', ArticleView.as_view(), name= 'article'),# view article /everyone
    path('event/', EventView.as_view(), name='event'), #view event /everyone
    path('post-event/', EventSerializerView.as_view()), #post article by superadmin and president only
    path('<id>/profile/', ProfileAPI.as_view()), #single profile view for authenticated user (creditantial not displayed
    path('upload-gallery/', CreateGalleryView.as_view()),#by president
    path('gallery/', GalleryView.as_view()), #everone
    path('contact-president/', ContactPresidentView.as_view()), #member can send message
    path('view-message/', ContactPresidentMessageView.as_view()), #president and admin can view the message

    path('<id>/', SinglePictureView.as_view()),
              ] + r.urls
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import ClubViewSet, home
from .event.views import  EventSerializerView
from .article.views import ArticleSerializerView

from .accounts.views import AdminRegistrationView, MemberApplicationRecordSerializerView, StaffLoginView, MemberLoginView, LogoutView
r = DefaultRouter()
# r.register('clubs,', ClubViewSet)


urlpatterns = [
    # path('clubs/', ClubViewSet.as_view,
    # path('signup/staff/', StaffRegistrationView.as_view()),
    path('member/', MemberApplicationRecordSerializerView.as_view(), name= 'member-applicaion'),
    path('login/', obtain_auth_token, name='login'),
    path('login/staff/', StaffLoginView.as_view(), name='login/staff'),
    path('login/member/', MemberLoginView.as_view(), name='login/member'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),
    # path('post/', EventPostView.as_view()),
    path('event/', EventSerializerView.as_view()),
    path('article/', ArticleSerializerView.as_view()),

                  # path('admin/', AdminClubViewSet.as_)
] + r.urls
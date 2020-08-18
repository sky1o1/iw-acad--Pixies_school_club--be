from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from club.models import ContactPresident
from .serializers import ContactPresidentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404


# FOR CREATING MESSAGE TO PRESIDENT
class ContactAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    serializer_class = ContactPresidentSerializer
    queryset = ContactPresident.objects.all()
 
    def post(self,request):
        return self.create(request)

   
#    FOR VIEWING NEWS IN STUDENT PANAL
# FROM HERE __________ COMMENT FOR USE
class NewsAPIView(generics.ListAPIView, mixins.ListModelMixin):
    serializer_class_news = NewsSerializer
    queryset = News.objects.all()

    def get(self,request):
        return self.list(request)
    
    
#    FOR VIEWING EVENTS IN STUDENT PANAL
class EventAPIView(generics.ListAPIView, mixins.ListModelMixin):
    serializer_class_event = EventSerializer
    queryset =Event.objects.all()

    def get(self,request):
        return self.list(request)


# FOR LEAVIING THE CLUB
class LeaveClubAPIView(generics.DestroyAPIView,mixins.DestroyModelMixin):
    serializer_class_leave_club = MyClubSerializer
    queryset = MyClub.objects.all()
    lookup_field = 'id'
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def delete(self,request, id):
            return self.destroy(request, id)






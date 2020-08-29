from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.views.generic import FormView
from .models import Club


User = get_user_model()


def home(request):
    return render(request, 'club/home.html')





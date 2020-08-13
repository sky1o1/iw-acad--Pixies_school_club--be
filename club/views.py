from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.views.generic import FormView
from django.contrib.auth.views import LoginView

from .loginforms import LoginAdminForm, LoginMemberForm, LoginStaffForm
from .signupforms import SignupAdminForm
from .models import Club
from .serializers import ClubSerializer

User = get_user_model()


class LoginAdminViewSet(LoginView):
    form_class = LoginAdminForm
    template_name = 'club/login.html'
    extra_context = {'form': form_class}

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            print('user is found', user)
            login(self.request, user)
            return redirect('/home/')
        else:
            print('user not verified', user)
            return HttpResponse('user not found')


class SignupAdminViewSet(FormView):
    form_class = SignupAdminForm
    template_name = 'club/signup.html'
    extra_context = {'form': form_class}

    def form_valid(self, form):
        username = form.cleaned_data['username'],
        first_name = form.cleaned_data['first_name'],
        middle_name = form.cleaned_data['middle_name'],
        last_name = form.cleaned_data['last_name'],
        email = form.cleaned_data['email'],
        password = form.cleaned_data['password'],
        user = User(
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email
            )
        user.save()
        user.set_password(password)
        user.save()

        logout(self.request)
        login(self.request, user)

        return redirect('/login/admin/')

    def get(self, request, *args, **kwargs):
        return render(request, 'club/signup.html', {'form': SignupAdminForm()})


def home(request):
    return render(request, 'club/home.html')


class ClubViewSet(ViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()






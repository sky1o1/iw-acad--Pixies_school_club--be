from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import AdminRegistrationSerializer, StaffRegistrationSerializer, MemberRegistrationSerializer

User = get_user_model()


class AdminRegistrationView(CreateAPIView):
    serializer_class = AdminRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # token = Token.objects.get(user=User).key
        return Response(serializer.data,   status=status.HTTP_201_CREATED)

#
# @api_view(['POST', ])
# def signup_view(request):
#     if request.method == 'POST':
#         serializer = LoginAdminSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             data = serializer.errors
#         return Response(data)


class StaffRegistrationView(CreateAPIView):
    serializer_class = StaffRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MemberRegistrationView(CreateAPIView):
    serializer_class = MemberRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class LoginAdminViewSet(LoginView):
#     form_class = LoginAdminForm
#     template_name = 'club/login.html'
#     extra_context = {'form': form_class}
#
#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#
#         if user:
#             print('user is found', user)
#             login(self.request, user)
#             return redirect('/home/')
#         else:
#             print('user not verified', user)
#             return HttpResponse('user not found')

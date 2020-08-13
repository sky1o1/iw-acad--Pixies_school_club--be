from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView

from .serializers import LoginAdminSerializer

User = get_user_model()


# class SignUpdminView(APIView):
#     @staticmethod
#     def post(self, request):
#         if request.method == 'POST':
#             serializer = LoginAdminSerializer(request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', ])
def signup_view(request):
    if request.method == 'POST':
        serializer = LoginAdminSerializer(request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
        return Response(data)


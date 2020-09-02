from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


from .serializers import ArticleSerializer, ViewArticleSerializer
from club.models import Article

User = get_user_model()
class ArticleSerializerView(CreateAPIView):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        data['response'] = 'Successfully Posted'
        data['article_title'] = article.article_title
        data['article_description'] = article.article_description
        # data['created_by_staff'] = article.created_by_staff
        # data['created_by_member'] = article.created_by_member
        data['all'] = article.all
        return Response(data, status=status.HTTP_201_CREATED)

class ArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ViewArticleSerializer
    permission_classes = [AllowAny, ]






from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from club.permissions import IsStaffUser, IsSuperUser
from rest_framework.response import Response
from .serializers import ArticleSerializer, ViewArticleSerializer
from club.models import Article
from rest_framework.permissions import AllowAny

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
        data['created_by'] = article.created_by
        return Response(data, status=status.HTTP_201_CREATED)


class ArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ViewArticleSerializer
    permission_classes = [AllowAny, ]






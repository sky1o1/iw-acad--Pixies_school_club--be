from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['article_title', 'article_description', 'created_by']

    def create(self, validated_data):
        user = Article(
            article_title=self.validated_data['article_title'],
            article_description=self.validated_data['article_description'],

            # all=self.validated_data['all'],
             #created_by=self.validated_data['created_by'],


        )

        user.save()
        return user


class ViewArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id','article_title', 'article_description', 'created_by']

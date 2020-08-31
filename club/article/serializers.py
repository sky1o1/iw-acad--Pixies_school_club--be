from rest_framework import serializers
from django.contrib.auth import get_user_model

from club.models import Article



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['article_title', 'article_description', 'all', 'created_by_staff', 'created_by_member']

    def create(self, validated_data):
        user = Article(
            article_title=self.validated_data['article_title'],
            article_description=self.validated_data['article_description'],
            # created_by_staff=self.validated_data['created_by_staff'],
            # created_by_member = self.validated_data['created_by_member'],

            all=self.validated_data['all'],

        )

        user.save()
        return user

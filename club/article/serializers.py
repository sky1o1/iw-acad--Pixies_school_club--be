from rest_framework import serializers
from club.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['article_title', 'article_description', 'created_by']

    def create(self, validated_data):
        user = Article(
            article_title=self.validated_data['article_title'],
            article_description=self.validated_data['article_description'],
            created_by=self.validated_data['created_by'],
        )

        user.save()
        return user


class ViewArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id','article_title', 'article_description', 'created_by']

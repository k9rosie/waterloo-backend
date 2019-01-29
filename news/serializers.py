from rest_framework import serializers

from .models import Article
from users.serializers import UserShortSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    authors = UserShortSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        lookup_field = 'slug'
        fields = ['authors', 'title', 'image', 'image_width', 'image_height', 'standfirst', 'body', 'created_at', 'slug']

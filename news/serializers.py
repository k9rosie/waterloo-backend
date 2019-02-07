from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='user-detail')

    class Meta:
        model = Article
        lookup_field = 'slug'
        fields = ['id', 'url', 'image_width', 'image_height', 'image', 'title', 'standfirst', 'body', 'authors', 'created_at', 'slug']

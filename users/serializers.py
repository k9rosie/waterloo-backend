from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='review-detail')
    articles = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='article-detail')

    class Meta:
        model = User
        lookup_field = 'slug'
        fields = ('id', 'url', 'name', 'bio', 'reviews', 'articles', 'created_at', 'slug')

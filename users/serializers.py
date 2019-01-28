from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(many=True, view_name='review-detail', read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        lookup_field = 'slug'
        fields = ('url', 'id', 'reviews', 'articles', 'name', 'bio', 'slug')

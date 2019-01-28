from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        lookup_field = 'slug'
        fields = '__all__'

from rest_framework import serializers

from .models import Genre, Label, Artist, Album


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        lookup_field = 'slug'
        fields = '__all__'


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        lookup_field = 'slug'
        fields = '__all__'


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        lookup_field = 'slug'
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


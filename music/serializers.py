from rest_framework import serializers

from .models import Genre, Label, Artist, Album


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        lookup_field = 'slug'
        fields = ['name', 'slug', 'artists', 'albums']


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        lookup_field = 'slug'
        fields = ['name', 'slug', 'artists', 'albums']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        lookup_field = 'slug'
        fields = ['name', 'slug', 'image_width', 'image_height', 'image', 'bio', 'deans_list', 'genres', 'labels']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'cover_width', 'cover_height', 'cover', 'artists', 'genres', 'labels', 'release_date', 'review']


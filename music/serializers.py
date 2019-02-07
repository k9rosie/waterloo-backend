from rest_framework import serializers

from .models import Genre, Label, Artist, Album


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    albums = serializers.HyperlinkedRelatedField(many=True, view_name='album-detail')
    genres = serializers.HyperlinkedRelatedField(many=True, view_name='genre-detail')

    class Meta:
        model = Genre
        lookup_field = 'slug'
        fields = ['id', 'url', 'name', 'albums', 'genres', 'slug']


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(many=True, view='artist-detail')
    albums = serializers.HyperlinkedRelatedField(many=True, view='album-detail')

    class Meta:
        model = Label
        lookup_field = 'slug'
        fields = ['id', 'url', 'name', 'artists', 'albums', 'slug']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = serializers.HyperlinkedRelatedField(many=True, view='album-detail')

    class Meta:
        model = Artist
        lookup_field = 'slug'
        fields = ['id', 'url', 'name', 'image_width', 'image_height', 'image', 'bio', 'genres', 'labels', 'deans_list', 'slug']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(view_name='review-detail')

    class Meta:
        model = Album
        lookup_field = 'slug'
        fields = ['id', 'url', 'name', 'cover_width', 'cover_height', 'cover', 'review', 'artists', 'genres', 'labels', 'release_date']

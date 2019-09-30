from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Genre, Label, Artist, Album

char_field_default_filters = ['exact', 'icontains', 'istartswith', 'iendswith', 'regex', 'iregex']
date_default_filters = ['range', 'year', 'iso_year', 'month', 'day', 'week', 'week_day', 'quarter']


class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = ['name', 'artists', 'albums']
        interfaces = (relay.Node,)


class LabelNode(DjangoObjectType):
    class Meta:
        model = Label
        filter_fields = {
            'id': ['exact'],
            'name': char_field_default_filters,
        }
        interfaces = (relay.Node,)


class ArtistNode(DjangoObjectType):
    class Meta:
        model = Artist
        filter_fields = {
            'id': ['exact'],
            'name': char_field_default_filters,
            'bio': char_field_default_filters[:-4],
            'deans_list': ['exact'],
            'labels': char_field_default_filters,
            'genres': char_field_default_filters
        }
        interfaces = (relay.Node,)


class AlbumNode(DjangoObjectType):
    class Meta:
        model = Album
        filter_fields = {
            'id': ['exact'],
            'name': char_field_default_filters,
            'artists': char_field_default_filters,
            'genres': char_field_default_filters,
            'labels': char_field_default_filters,
            'release_date': date_default_filters
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    genre = relay.Node.Field(GenreNode)
    all_genres = DjangoFilterConnectionField(GenreNode)

    label = relay.Node.Field(LabelNode)
    all_labels = DjangoFilterConnectionField(LabelNode)

    artist = relay.Node.Field(ArtistNode)
    all_artists = DjangoFilterConnectionField(ArtistNode)

    album = relay.Node.Field(AlbumNode)
    all_albums = DjangoFilterConnectionField(AlbumNode)

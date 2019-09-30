from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Genre, Label, Artist, Album


class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = ['name', 'artists', 'albums']
        interfaces = (relay.Node,)

class ArtistNode(DjangoObjectType):
    class Meta:
        model = Artist
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'bio': ['exact', 'icontains', 'istartswith'],
            'deans_list': ['exact'],
            'labels': ['exact', 'icontains', 'istartswith'],
            'genres': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)

class AlbumNode(DjangoObjectType):
    class Meta:
        model = Album
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'artists': ['exact', 'icontains', 'istartswith'],
            'genres': ['exact', 'icontains', 'istartswith'],
            'labels': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    genre = relay.Node.Field(GenreNode)
    all_genres = DjangoFilterConnectionField(GenreNode)

    artist = relay.Node.Field(ArtistNode)
    all_artists = DjangoFilterConnectionField(ArtistNode)

    album = relay.Node.Field(AlbumNode)
    all_albums = DjangoFilterConnectionField(AlbumNode)


from rest_framework import viewsets, permissions

from .models import Genre, Label, Artist, Album
from .serializers import GenreSerializer, LabelSerializer, ArtistSerializer, AlbumSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

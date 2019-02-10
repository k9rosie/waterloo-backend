from rest_framework import viewsets, permissions

from .models import Genre, Label, Artist, Album
from .serializers import GenreSerializer, LabelSerializer, ArtistSerializer, AlbumSerializer


class GenreViewset(viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class LabelViewset(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ArtistViewset(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

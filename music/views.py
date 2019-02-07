from rest_framework import viewsets, permissions

from .models import Genre, Label, Artist, Album


class GenreViewset(viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = Genre
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class LabelViewset(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = Label
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ArtistViewset(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = Artist
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = Album
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

from django.db import models
from django.utils.crypto import get_random_string


class Genre(models.Model):
    id = models.CharField(primary_key=True, default=get_random_string, editable=False, max_length=8)
    name = models.CharField(unique=True, max_length=16)
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    id = models.CharField(primary_key=True, default=get_random_string, editable=False, max_length=8)
    name = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    id = models.CharField(primary_key=True, default=get_random_string, editable=False, max_length=8)
    name = models.CharField(unique=True, max_length=200)
    image_width = models.IntegerField(default=1600, blank=True)
    image_height = models.IntegerField(default=1600, blank=True)
    image = models.ImageField(upload_to='artist_imgs', height_field='image_width', width_field='image_height', blank=True)
    bio = models.TextField(blank=True)
    deans_list = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, related_name='artists', blank=True)
    labels = models.ManyToManyField(Label, related_name='artists', blank=True)
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.CharField(primary_key=True, default=get_random_string, editable=False, max_length=8)
    name = models.CharField(max_length=200)
    cover_width = models.IntegerField(default=1600, blank=True)
    cover_height = models.IntegerField(default=1600, blank=True)
    cover = models.ImageField(upload_to='album_imgs', height_field='cover_height', width_field='cover_width', blank=True)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=False)
    genres = models.ManyToManyField(Genre, related_name='albums', blank=False)
    labels = models.ManyToManyField(Label, related_name='albums', blank=True)
    release_date = models.DateField()

    def get_genres(self):
        return "\n".join([g.name for g in self.genres.all()])
    get_genres.short_description = 'Genres'

    def get_labels(self):
        return "\n".join([l.name for l in self.labels.all()])
    get_labels.short_description = 'Labels'

    def get_artists(self):
        return "\n".join([a.name for a in self.artists.all()])
    get_artists.short_description = 'Artists'

    def __str__(self):
        return self.name

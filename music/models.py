from django.db import models


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=16)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to='artist_imgs', height_field=1600, width_field=1600, blank=True)
    genres = models.ManyToManyField(Genre)
    bio = models.TextField(blank=True)
    deans_list = models.BooleanField(default=False)

    def get_genres(self):
        return "\n".join([g.name for g in self.genres.all()])
    get_genres.short_description = 'Genres'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    cover_width = models.IntegerField(default=1600, blank=True)
    cover_height = models.IntegerField(default=1600, blank=True)
    cover = models.ImageField(upload_to='album_imgs', height_field='cover_height', width_field='cover_width', blank=True)
    artists = models.ManyToManyField(Artist, blank=False)
    genres = models.ManyToManyField(Genre, blank=False)
    labels = models.ManyToManyField(Label, blank=True)
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

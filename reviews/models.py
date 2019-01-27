from django.db import models
from accounts.models import User
from music.models import Album

# Create your models here.
class Review(models.Model):
    RATINGS = (
        ('S', 'S'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F')
    )
    authors = models.ManyToManyField(User)
    rating = models.CharField(max_length=2, choices=RATINGS, default='F')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    standfirst = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def album_name(self):
        return self.album.name

    def album_artists(self):
        return "\n".join([a.name for a in self.album.artists.all()])

    def written_by(self):
        return "\n".join([a.first_name + a.last_name])

    def __str__(self):
        return self.album.name


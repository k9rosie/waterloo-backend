from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from users.models import User


class Article(models.Model):
    id = models.CharField(primary_key=True, default=get_random_string, editable=False, max_length=8)
    authors = models.ManyToManyField(User, related_name='articles')
    title = models.CharField(max_length=280)
    image_width = models.IntegerField(default=1600, blank=True)
    image_height = models.IntegerField(default=1600, blank=True)
    image = models.ImageField(upload_to='artist_imgs', height_field='image_width', width_field='image_height',
                              blank=True)
    standfirst = models.TextField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, blank=True)
    carousel = models.BooleanField(default=False)
    top_story = models.BooleanField(default=False)

    def article_authors(self):
        return "\n".join([a.name for a in self.authors.all()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(self, *args, **kwargs)

    def __str__(self):
        return self.title

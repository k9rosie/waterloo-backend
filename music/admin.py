from django.contrib import admin
from django.utils.html import mark_safe

from .models import Genre, Label, Artist, Album


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('slug',)


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('slug',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('slug',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_display = ('name', 'get_artists', 'get_labels', 'release_date',)
    list_filter = ('genres__name',)
    readonly_fields = ['cover_image']
    search_fields = ('name', 'artists__name', 'labels__name',)
    autocomplete_fields = ['artists', 'labels', 'genres']

    def cover_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.cover.url,
            width=obj.cover.width,
            height=obj.cover.height,
            )
        )


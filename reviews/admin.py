from django.contrib import admin

from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('album_name', 'album_artists', 'review_authors', 'rating', 'created_at')
    autocomplete_fields = ['authors', 'album']
    readonly_fields = ('slug',)


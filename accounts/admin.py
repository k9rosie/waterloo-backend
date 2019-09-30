from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'email', 'created_at', 'last_login', 'is_superuser')
    list_filter = ('is_superuser',)
    prepopulated_fields = {'slug': ('name',), }
    fieldsets = (
        (None, {'fields': ('email', 'name', 'bio', 'password', 'slug')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'slug')
        }),
    )

    search_fields = ('email', 'name', )
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

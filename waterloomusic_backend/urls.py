"""waterloomusic_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from rest_framework_swagger.views import get_swagger_view

from news.views import ArticleViewset
from reviews.views import ReviewViewset
from users.views import UserViewset
from music.views import AlbumViewset, ArtistViewset, LabelViewset, GenreViewset

schema_view = get_schema_view(title='Waterloo Music Academy API')
docs_view = get_swagger_view(title='Waterloo Music Academy API')

router = DefaultRouter()
router.register(r'articles', ArticleViewset)
router.register(r'reviews', ReviewViewset)
router.register(r'users', UserViewset)
router.register(r'albums', AlbumViewset)
router.register(r'artists', ArtistViewset)
router.register(r'labels', LabelViewset)
router.register(r'genres', GenreViewset)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'docs/', docs_view),
    path(r'schema/', schema_view),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
from django.conf.urls import url
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from news.views import ArticleViewSet
from reviews.views import ReviewViewSet
from users.views import UserViewSet
from music.views import AlbumViewSet, ArtistViewSet, LabelViewSet, GenreViewSet

schema_view = get_swagger_view(title='Waterloo Music Academy API')
docs_view = include_docs_urls(title='Waterloo Music Academy API')

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'labels', LabelViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'docs/', docs_view),
    path(r'schema/', schema_view),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

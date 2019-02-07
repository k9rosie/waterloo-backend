from rest_framework import permissions, viewsets

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

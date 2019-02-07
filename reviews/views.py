from rest_framework import permissions, viewsets

from .models import Review

from .serializers import ReviewSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

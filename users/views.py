from rest_framework import permissions, viewsets

from .models import User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

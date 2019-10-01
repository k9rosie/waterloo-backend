from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'bio': ['icontains'],
            'created_at': ['year', 'iso_year'],
            'is_staff': ['exact']
        }
        interface = (relay.Node,)


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

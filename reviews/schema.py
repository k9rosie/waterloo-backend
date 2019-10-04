from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Review


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        filter_fields = ['id', 'authors', 'rating', 'album', 'standfirst', 'body', 'created_at']
        interfaces = (relay.Node,)


class Query(ObjectType):
    review = relay.Node.Field(ReviewNode)
    all_reviews = DjangoFilterConnectionField(ReviewNode)

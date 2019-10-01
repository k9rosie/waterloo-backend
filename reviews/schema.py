from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Review


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        filter_fields = {
            'id': ['exact'],
            'authors': ['icontains', 'regex'],
            'rating': ['exact'],
            'album': ['icontains', 'regex'],
            'standfirst': ['icontains'],
            'body': ['icontains'],
            'created_at': ['range', 'year', 'iso_year', 'month', 'day', 'week', 'week_day', 'quarter']
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    review = relay.Node.Field(ReviewNode)
    all_reviews = DjangoFilterConnectionField(ReviewNode)

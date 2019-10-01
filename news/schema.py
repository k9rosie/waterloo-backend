from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Article

class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'id': ['exact'],
            'authors': ['icontains'],
            'title': ['icontains', 'istartswith', 'iendswith', 'regex'],
            'standfirst': ['icontains'],
            'body': ['icontains'],
            'created_at': ['range', 'year', 'iso_year', 'month', 'day', 'week', 'week_day', 'quarter'],
            'frontpage': ['exact']
        }
        interfaces = (relay.Node,)

class Query(ObjectType):
    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
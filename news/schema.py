from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Article


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ['id', 'authors', 'title', 'standfirst', 'body', 'created_at', 'frontpage']
        interfaces = (relay.Node,)


class Query(ObjectType):
    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)

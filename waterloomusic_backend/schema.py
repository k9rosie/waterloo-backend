import graphene

import accounts.schema
import music.schema
import news.schema
import reviews.schema


class Query(accounts.schema.Query, music.schema.Query,
            news.schema.Query, reviews.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

import graphene
from blog.api.graph import Query as BlogQuery


class Query(BlogQuery, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query)
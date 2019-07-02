import graphene
from blog.api.graph import Query as BlogQuery
from blog.api.graph import Mutation as BlogMutation

class Query(BlogQuery, graphene.ObjectType):
	pass

class Mutation(BlogMutation, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query, mutation=Mutation)
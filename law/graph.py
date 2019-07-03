from blog.api.schema import Query as BlogQuery
from blog.api.schema import Mutation as BlogMutation

from graphene import ObjectType, Schema

class Query(BlogQuery, ObjectType):
	pass

class Mutation(BlogMutation, ObjectType):
	pass


schema = Schema(query=Query, mutation=Mutation)
from blog.graph.schema import Query as BlogQuery
from blog.graph.schema import Mutation as BlogMutation

from graphene import ObjectType, Schema as _SCHEMA

class Query(BlogQuery, ObjectType):
	pass

class Mutation(BlogMutation, ObjectType):
	pass


schema = _SCHEMA(query=Query, mutation=Mutation)

from json import dumps, loads
def execute(query):
	return dumps(schema.execute(query).data)
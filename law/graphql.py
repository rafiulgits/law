from blog.graph.schema import Query as BlogQuery
from blog.graph.schema import Mutation as BlogMutation

from exam.graph.schema import Query as ExamQuery
from exam.graph.schema import Mutation as ExamMutation

from graphene import ObjectType, Schema as _SCHEMA

class Query(BlogQuery, ExamQuery, ObjectType):
	pass

class Mutation(BlogMutation, ExamMutation, ObjectType):
	pass


schema = _SCHEMA(query=Query, mutation=Mutation)

from json import dumps, loads
def execute(query):
	return dumps(schema.execute(query).data)
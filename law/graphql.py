from account.graph.schema import Query as AccountQuery

from blog.graph.schema import Query as BlogQuery
from blog.graph.schema import Mutation as BlogMutation

from exam.graph.schema import Query as ExamQuery

from draft.graph.schema import Query as DraftQuery

from graphene import ObjectType, Schema as _SCHEMA

class Query(AccountQuery, BlogQuery, ExamQuery, DraftQuery, ObjectType):
	pass

class Mutation(BlogMutation, ObjectType):
	pass


schema = _SCHEMA(query=Query, mutation=Mutation)

from json import dumps, loads
def execute(query):
	return dumps(schema.execute(query).data)
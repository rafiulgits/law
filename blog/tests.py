from django.test import TestCase

import json
from law.graph import schema
from graphene_django.utils.testing import GraphQLTestCase

import json
from graphene_django.utils.testing import GraphQLTestCase
from law.graph import schema

class Hello(GraphQLTestCase):
	GRAPHQL_SCHEMA = schema
	print(schema)
	def test_some_query(self):
		response = self.query(
			'''
			query{
			  allFolders{
			    edges{
			      node{
			        name
			        distance
			        id
			      }
			    }
			  }
			}
									
			''',
			op_name = 'product'
		)
		print(response.content)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

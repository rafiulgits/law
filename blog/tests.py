from django.test import TestCase

import json
from law.graph import schema
from graphene_django.utils.testing import GraphQLTestCase

class MyText(GraphQLTestCase):
	GRAPHQL_SCHEMA = schema

	def test_some_query(self):
		response = self.query(
			'''
				query {
				  folder(selfLoc:9){
				    postSet{
				      title
				      body
				    }
				  }
				}
			''',
			
			)

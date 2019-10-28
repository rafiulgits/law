from law.graphql import execute


class Query():

	def all_subjects():
		query = """
			query {
			  allFolders(category_Name_Icontains:"Subject"){
			    edges{
			      node{
			        name
			        distance
			        selfLoc{
			          id
					  uid
			        }
			      }
			    }
			  }
			}
		"""
		return execute(query)


	def explore_folder(rootLoc=None, rootLocUid=None):
		if rootLoc:
			self_loc_query = 'selfLoc:"{}"'.format(rootLoc)
			root_loc_query = 'rootLoc:"{}"'.format(rootLoc)
		elif rootLocUid:
			self_loc_query = 'selfLocUid:{}'.format(rootLocUid)
			root_loc_query = 'rootLoc_Uid:{}'.format(rootLocUid)
		else:
			return None
		query = """
			query {{
			  folder({}) {{
			  	selfLoc {{
			      id
			      uid
			    }}
			    rootLoc {{
		          id
		          uid
		        }}
			    name
			    distance
			    category {{
			      name
			    }}
			  }}
			  allFolders({}) {{
			    edges {{
			      node {{
			        name
			        distance
			        category {{
			          name
			        }}
			        selfLoc {{
			          id
					  uid
			        }}
			        postSet {{
			          uid
			          title
			        }}
			      }}
			    }}
			  }}
			}}
		""".format(self_loc_query, root_loc_query)
		return execute(query)


	def get_post(uid):
		query = """
			query {{
			  post( uid: {} ){{
			  	uid
			    title
			    body
			    dateTime
			  }}
			}}

		""".format(uid)
		return execute(query)


	def mcq_list(after=None, before=None):
		params = "first:10"
		if after:
			params = """{}, after:"{}" """.format(params, after)
		elif before:
			params = """{}, before:"{}" """.format(params, before)
		query = """
			query {{
			  allMcqs ( {} ) {{
			    pageInfo {{
			      hasNextPage
			      hasPreviousPage
				  startCursor
				  endCursor
			    }}
			    edges {{
			      node {{ 
			        id
			        uid
			        question
			        option1
			        option2
			        option3
			        option4
			        answer
			        summary
			        mcqtagSet {{
					  edges {{
					    node {{
						  folder{{
							id
							name
							selfLoc{{
							  id
							  uid
							}}
						  }}
						}}
					  }}
					}}
			      }}
			    }}
			  }}
			}}
		""".format(params)
		return execute(query)


	def get_issue(uid):
		query = """
			query {{
			  mcqIssue(uid: {} ){{
			    id
			    uid
			    body
			    isSolved
			    user {{
			      id
			      name
			    }}
			  }}
			}}
		""".format(uid)
		return execute(query)
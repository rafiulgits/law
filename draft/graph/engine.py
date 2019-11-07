from law.graphql import execute

class Query:

	def root_directories():
		query = """
		query{
		  allDirectories(rootLoc:"null"){
		    edges{
		      node{
		        name
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


	def explore_directory(rootLoc=None, rootLocUid=None):
		if rootLoc:
			self_loc_query = 'selfLoc:"{}"'.format(rootLoc)
			root_loc_query = 'rootLoc:"{}"'.format(rootLoc)
		elif rootLocUid:
			self_loc_query = 'selfLocUid:"{}"'.format(rootLocUid)
			root_loc_query = 'rootLoc_Uid:"{}"'.format(rootLocUid)
		else:
			return None
		query = """
			query {{
			  directory({}) {{
			  	selfLoc {{
			      id
			      uid
			    }}
			    rootLoc {{
		          id
		          uid
		        }}
			    name
			    articleSet {{
		          uid
		          title
		          dateTime
		        }}
			  }}
			  allDirectories({}) {{
			    edges {{
			      node {{
			        name
			        selfLoc {{
			          id
					  uid
			        }}
			      }}
			    }}
			  }}
			}}
		""".format(self_loc_query, root_loc_query)
		return execute(query)


	def article(uid):
		query = """
		  query {{
			article( uid:"{}" ) {{
			  uid
			  title
			  body
			  dateTime
			  lastUpdate
			  }}
			}}
		""".format(uid)
		return execute(query)


	def all_articles(after=None, before=None):
		filter = "first:20"
		if after:
			filter = '{} after="{}"'.format(filter, after)
		query = """
			query {{
				allArticle({}) {{
					pageInfo {{
					startCursor
					endCursor
					hasNextPage
					hasPreviousPage
					}}
					edges {{
						node {{
							id
							uid
							title
						}}
					}}
				}}
			}}
		""".format(filter)
		return execute(query)
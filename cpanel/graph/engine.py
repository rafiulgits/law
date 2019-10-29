from law.graphql import execute

class Query:
	def all_users(page=1):
		query = """
			query {{
			  allAccounts(page:{}) {{
			    name
			    phone
			    email
			    gender
			    profile {{
			      bar
			      session
			      institute
			    }}
			  }}
			}}
		""".format(page)
		return execute(query)



	def all_issues(before=None, after=None):
		query = """
			query{
			  allMcqIssues{
			    pageInfo{
			      hasNextPage
			      hasPreviousPage
			      startCursor
			      endCursor
			    }
			    edges{
			      node{
			        uid
			        body
			        dateTime
			        isSolved
			        user{
			          name
			        }
			        mcq{
			          uid
			        }
			      }
			    }
			  }
			}
		"""
		return execute(query)
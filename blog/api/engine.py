from law.graphql import execute

class Query():

	def all_subjects():
		query = """
			query {
			  allFolders(category_Name_Icontains:"Subject"){
			    edges{
			      node{
			        name
			        selfLoc{
			          id
			        }
			      }
			    }
			  }
			}
		"""
		return execute(query)

	def explore_folder(rootLoc):
		query = """
			query {{
			  allFolders(rootLoc:"{}") {{
			    edges {{
			      node {{
			        name
			        category {{
			          name
			        }}
			        selfLoc {{
			          id
			        }}
			        postSet {{
			          uid
			          title
			        }}
			      }}
			    }}
			  }}
			}}
		""".format(rootLoc)
		
		return execute(query)

	def get_post(uid):
		query = """
			query {{
			  post( uid: {} ){{
			    title
			    body
			    dateTime
			  }}
			}}

		""".format(uid)
		return execute(query)
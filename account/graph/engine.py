from law.graphql import execute


class Query:

	def profile(account_id):
		query = """
			query {{
			  account(id:{}) {{
			    id
			    name
			    phone
			    email
			    isStaff
			    isSuperuser
			    profile {{
			      institute
			      bar
			      session
			    }}
			  }}
			}}
		""".format(account_id)
		return execute(query)

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
			  folder(selfLoc:"{}") {{
			  	selfLoc {{
			      id
			      uid
			    }}
			    name
			    distance
			    category {{
			      name
			    }}
			  }}
			  allFolders(rootLoc:"{}") {{
			    edges {{
			      node {{
			        name
			        distance
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
		""".format(rootLoc, rootLoc)
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




class Mutation():

	def create_folder(data):
		rootLoc = None
		if data.get('root_loc', None):
			rootLoc = ",rootLocUid:{}".format(data['root_loc'])
		else:
			rootLoc = ""

		query = """
			mutation {{
			  createFolder(name:"{}", categoryName:"{}", distance:{} {}) {{
			    folder {{
			      name
			      distance
			      category {{
			        name
			      }}
			      selfLoc {{
			        id
			        uid
			      }}
			    }}
			  }}
			}}
		""".format(data['name'], data['category'], data['distance'], rootLoc)
		return execute(query)


	def create_post(data):
		query = """
			mutation {{
			  createPost(title:"{}", body: "{}", folderLoc: {} ) {{
			    post {{
			      uid
			      title
			      body
			      dateTime
			    }}
			  }}
			}}
		""".format(data['title'], data['body'], data['folder'].self_loc)
		return execute(query)


	def create_mcq(data):
		query = """
		mutation {{
		  createMcq(
		    question:"{}", option1:"{}", option2:"{}", option3:"{}", option4:"{}",
		  	answer:{}, summary:"{}", level:{} ) {{
		    mcq {{
		      question
		      option1
		      option2
		      option3
		      option4
		      answer
		      summary
		      level
		    }}
		  }}
		}}

		""".format(data['question'], data['option1'], data['option2'], data['option3'],
			data['option4'], data['answer'],data['summary'], data['level'])
		return execute(query)
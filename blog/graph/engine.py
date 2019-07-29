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






class Mutation():

	def create_folder(name, category_name, distance, rootLoc_uid):
		rootLoc = None
		if rootLoc_uid:
			rootLoc = ",rootLocUid:{}".format(rootLoc_uid)
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
			      postSet {{
			        uid
			        title
			      }}
			    }}
			  }}
			}}
		""".format(name, category_name, distance, rootLoc)
		return execute(query)


	def create_post(title, body, folder_loc):
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
		""".format(title, body, folder_loc)
		return execute(query)


	def create_mcq(ques,op1,op2,op3,op4,ans,summary,level):
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

		""".format(ques,op1,op2,op3,op4,ans,summary,level)
		return execute(query)
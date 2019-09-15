from law.graphql import execute


class Create():
	def folder(data):
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


	def post(data):
		query = """
			mutation {{
			  createPost(title:"{}", body: "{}", folderLoc: {} ) {{
			    post {{
			      uid
			      title
			    }}
			  }}
			}}
		""".format(data['title'], data['body'], data['folder'].self_loc)
		return execute(query)


	def mcq(data):
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

	def mcq_tag(data):
		query = """
			mutation {{
			  createMcqTag( folderLoc:{}, mcqUid:{}) {{
			    mcqTag {{
			      id
			      uid
			      folder {{
			        name
			      }}
			    }}
			  }}
			}}
		""".format(data['folder'].self_loc_id, data['mcq'].uid)
		return execute(query)



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



class Update():
	def folder(data):
		pass


	def post(data):
		pass


	def mcq(data):
		pass



class Delete():

	def folder(data):
		self_loc_uid = data.get('self_loc_uid', 0)
		query = """
			mutation {{
			  deleteFolder(selfLocUid:{}) {{
			    folder {{
			      name
			      distance
			      category {{
			        name
			      }}
			    }}
			  }}
			}}
		""".format(self_loc_uid)
		return execute(query)


	def post(data):
		post_uid = data.get('post_uid', 0)
		query = """
			mutation {{
			  deletePost(postUid:{}) {{
			    post {{
			      uid
			  		title
			    }}
			  }}
			}}
		""".format(post_uid)
		return execute(query)


	def mcq(data):
		mcq_uid = data.get('mcq_uid', 0)
		query = """
			mutation {{
			  deleteMcq(mcqUid:{}) {{
			    mcq {{
			      question
			      answer
			      summary
			    }}
			  }}
			}}
		""".format(mcq_uid)
		return execute(query)


	def mcq_tag(data):
		mcq_tag_uid = data.get('mcq_tag_uid', 0)
		query = """
			mutation {{
			  deleteMcqTag(mcqTagUid:{}) {{
			    mcqTag {{
			      mcq {{
			        uid
			      }}
			      folder {{
			        selfLoc {{
			          uid
			          id
			        }}
			      }}
			    }}
			  }}
			}}
		""".format(mcq_tag_uid)
		return execute(query)
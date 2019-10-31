from law.graphql import execute


class Query:

    def all_mcq_exams(**kwargs):
        query_filter = "isPublic:true, first:20"
        if kwargs.get('after', None):
          query_filter = '{} after:"{}"'.format(query_filter, kwargs.get('after'))
        query = """
            query {{
              allMcqExams( {} ) {{
                pageInfo {{
                  hasPreviousPage
                  hasNextPage
                  startCursor
                  endCursor
                }}
                edges {{
                  node {{
                    id
                    uid
                    name
                    isClone
                    isPublic
                    dateTime
                    createdBy {{
                      id
                      name
                    }}
                    source {{
                      totalMcq
                      duration
                      dateTime
                      createdBy {{
                        id
                        name
                      }}
                    }}
                  }}
                }}
              }}
            }}
        """.format(query_filter)
        return execute(query)


    def user_mcq_exams(user_id):
      query = """
        query {{
          allMcqExams(createdBy: {} ){{
            edges {{
              node {{
                uid
                name
                dateTime
                source {{
                  totalMcq
                  statistics
                }}
                mcqreport {{
                  totalCorrect
                }}
              }}
            }}
          }}
        }}
      """.format(user_id)
      return execute(query)


    def mcq_exam_preview(uid):
    	query = """
			query {{
			  mcqExam(uid: {} ) {{
          uid
			    name
          isClone
          isPublic
          createdBy {{
            id
            name
          }}
			    source {{
            id
			      uid
			      public
			      statistics
			      duration
			      dateTime
			      totalMcq
			      createdBy {{
			      	id
			        name
			      }}
			    }}
			    mcqreport {{
           id
			    }}
			  }}
			}}
    	""".format(uid)
    	return execute(query)


    def mcq_exam(uid):
      query = """
        query {{
          mcqExam(uid: {} ) {{
            source {{
            duration
              mcqexamitemSet {{
                edges {{
                  node {{
                    mcq {{
                      id
                      uid
                      question
                      option1
                      option2
                      option3
                      option4
                    }}
                  }}
                }}
              }}
            }}
          }}
        }}
      """.format(uid)
      return execute(query)


    def mcq_exam_report(exam_uid):
      query = """
        query {{
          mcqExam(uid: {} ) {{
            name
            isClone
            isPublic
            createdBy {{
              id
              name
            }}
            source {{
              id
              uid
              public
              statistics
              duration
              dateTime
              totalMcq
              createdBy {{
                id
                name
              }}
            }}
            mcqreport {{
              uid
              dateTime
              totalCorrect
              totalWrong
              totalBlank
              result
              omrSet {{
                edges {{
                  node {{
                    mcq {{
                      uid
                      question
                      answer
                      summary
                      option1
                      option2
                      option3
                      option4
                    }}
                    answer
                    correct
                  }}
                }}
              }}
            }}
          }}
        }}
      """.format(exam_uid)
      return execute(query)

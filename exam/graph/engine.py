from law.graphql import execute


class Query:
    def all_mcq_exams(**kwargs):
        query_filter = "isPublic:true"
        query = """
            query {{
              allMcqExams( {} ) {{
                edges {{
                  node {{
                    id
                    uid
                    name
                    isClone
                    isPublic
                    dateTime
                    createdBy {{
                      name
                    }}
                    source {{
                      totalMcq
                      duration
                      dateTime
                      createdBy {{
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


    def mcq_exam(uid):
      query = """
        query {{
          mcqExam(uid: {} ) {{
            id
            uid
            name
            isClone
            isPublic
            createdBy {{
              name
            }}
            source {{
              id
              uid
              duration
              statistics
              dateTime
              totalMcq
              createdBy {{
                name
              }}
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
              duration
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

from law.graphql import execute


class Mutation:

    def create_mcq_exam(data):
        if data['public']:
            data['public'] = 1
        else:
            data['public'] = 0

        query = """
            mutation {{
              createMcqExam(name:"{}", level:{}, totalMcq:{}, marks:{}, createdBy:{}, public:{}) {{
                mcqExam {{
                  id
                  uid
                  name
                  level
                  totalMcq
                  marks
                  dateTime
                  createdBy {{
                    id
                    name
                    phone
                    email
                    gender
                  }}
                  mcqexamitemSet {{
                    edges {{
                      node {{
                        mcq {{
                          question
                          option1
                          option2
                          option3
                          option4
                          answer
                          summary
                        }}
                      }}
                    }}
                  }}
                }}
              }}
            }}
        """.format(data['name'],data['level'],data['total_mcq'],data['marks'],
            data['created_by'].id, data['public'])
        return execute(query)


    def create_clone_mcq_exam(data):
        query = """
          mutation {{
            createCloneMcqExam(clonedBy:{},name:"{}", originUid:{}) {{
              cloneMcqExam {{
                id
                uid
                name
                dateTime
                origin {{
                  id
                  uid
                  name
                  totalMcq
                  marks
                  dateTime
                  createdBy {{
                    id
                    name
                    phone
                    email
                    gender
                  }}
                }}
                clonedBy {{
                  id
                  name
                  phone
                  email
                  gender
                }}
              }}
            }}
          }}
        """.format(data['cloned_by'].id, data['name'], data['origin'].uid)
        return execute(query)


    def create_mcq_exam_item(data):
        query = """
            mutation {{
              createMcqExamItem(examUid:{}, mcqUid:{}) {{
                mcqExamItem {{
                  id
                  uid
                  mcq {{
                    uid
                    question
                    option1
                    option2
                    option3
                    option4
                    answer
                    summary
                    level
                  }}
                  exam {{
                    id
                    uid
                    name
                    dateTime
                    totalMcq
                    marks
                    createdBy {{
                      name
                      phone
                      email
                      gender
                    }}
                  }}
                }}
              }}
            }}
        """.format(data['exam'].uid, data['mcq'].uid)
        return execute(query)



    def create_omr(data):
        query = """
            mutation {{
              createOmr(answer:{},mcqUid:{}, reportUid:{}) {{
                omr {{
                  id
                  uid
                  correct
                  mcq {{
                    question
                    answer
                  }}
                }}
              }}
            }}
        """.format(data['answer'], data['mcq'].uid, data['report'].uid)
        return execute(query)





class Query:

    def all_mcq_exams(**kwargs):
        query_filter = "public:true"
        user_id = kwargs.get('user_id', None)
        if user_id:
          query_filter = """{}, createdBy:{}""".format(query_filter, user_id)
        query = """
            query {{
              allMcqExams({}) {{
                edges {{
                  node {{
                    id
                    uid
                    name
                    dateTime
                    marks
                    totalMcq
                    createdBy {{
                      id
                      name
                    }}
                  }}
                }}
              }}
            }}
        """.format(query_filter)
        return execute(query)


    def mcq_exam(uid):
      query = """
        query {{
          mcqExam(uid:{}) {{
            id
            uid
            name
            dateTime
            marks
            totalMcq
            public
            createdBy {{
              id
              name
            }}
            mcqexamitemSet {{
              edges {{
                node {{
                  uid
                  mcq {{
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
      """.format(uid)
      return execute(query)

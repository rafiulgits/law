from law.graphql import execute

class Query:
    def article(uid):
        query = """
          query {{
            article( uid:"{}" ) {{
              id
              uid
              title
              body
              dateTime
              lastUpdate
              }}
            }}
        """.format(uid)
        return execute(query)
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

    
    def all_articles(after=None, before=None):
        filter = "first:20"
        if after:
            filter = '{} after="{}"'.format(filter, after)
        query = """
            query {{
                allArticle({}) {{
                    pageInfo {{
                    startCursor
                    endCursor
                    hasNextPage
                    hasPreviousPage
                    }}
                    edges {{
                        node {{
                            id
                            uid
                            title
                        }}
                    }}
                }}
            }}
        """.format(filter)
        return execute(query)
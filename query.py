from graphql import GraphQLClient
#client = GraphQLClient('https://api.thegraph.com/subgraphs/name/thomasproust/cryptokitties-explorer')
class molochClient():
    def __init__(self):
        self.client = GraphQLClient('https://api.thegraph.com/subgraphs/name/molochventures/moloch')
        self.result = self.client.execute('''
        {
        members(first: 1, orderDirection: desc) {
            id
            shares
            isActive
            didRagequit
            }
        }
        ''')

    def get(self):
        return self.result

class kittyClient():
    def __init__(self):
        self.client = GraphQLClient('https://api.thegraph.com/subgraphs/name/thomasproust/cryptokitties-explorer')
        self.result = self.client.execute('''
        {
            cryptoKitties( orderBy: birthTime, orderDirection: asc, first: 1,)
            {
            owner,
            birthTime
            }
        }
        ''')
    def get(self):
        return self.result
#print(result)

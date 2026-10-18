class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for from_i, to_i in tickets:
            graph[from_i].append(to_i)

        for key in graph:
            graph[key].sort(reverse=True)

        path = []

        def dfs(node):

            
            
            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)

            path.append(node)

        dfs("JFK")

        return path[::-1]


        

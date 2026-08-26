class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
       
        graph = defaultdict(list)
        for ticket in tickets:
            src, dest = ticket 
            graph[src].append(dest)

        for src, destinations in graph.items():
            destinations.sort(reverse=True)

        order = []

        def dfs(node):
            while graph[node]:
                dst = graph[node].pop()
                dfs(dst)
            order.append(node)

        dfs("JFK")
        return order[::-1]
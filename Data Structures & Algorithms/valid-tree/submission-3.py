class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False 

        graph = {}
        for i in range(n):
            graph[i] = []
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

        dfs(0)

        return len(visited) == n

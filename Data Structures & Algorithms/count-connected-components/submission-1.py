class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                if n in visited:
                    continue 
                dfs(n)

        count = 0 
        for v in graph:
            if v not in visited:
                dfs(v)
                count += 1

        return count

                
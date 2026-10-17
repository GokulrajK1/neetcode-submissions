class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}
        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(i):
            visited.add(i)
            for n in graph[i]:
                if n in visited: continue 
                dfs(n)

        count = 0
        for i in range(n):
            if i in visited: continue
            dfs(i)
            count += 1

        return count
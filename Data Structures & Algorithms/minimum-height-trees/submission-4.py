class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        graph = {}
        
        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        edges_count = {}
        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
            edges_count[i] = len(graph[i])

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for nei in graph[leaf]:
                    edges_count[nei] -= 1
                    if edges_count[nei] == 1:
                        leaves.append(nei)

        return [0]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(0, len(edges) + 1)]
        
        def union(u, v):
            parent[find(u)] = find(v)

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u, v)

        




        
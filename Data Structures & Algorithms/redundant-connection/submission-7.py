class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [x for x in range(0, len(edges) + 1)]
        rank = [0 for _ in range(len(edges) + 1)]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            rx, ry = find(u), find(v)
            if rx == ry: return False 

            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                rank[rx] += 1

            return True 

        for u, v in edges:
            if not union(u, v):
                return [u, v]
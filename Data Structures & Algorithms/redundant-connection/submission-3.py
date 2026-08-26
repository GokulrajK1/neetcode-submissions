class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(0, len(edges) + 1)]
        rank = [0] * (len(edges) + 1)
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False

            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                rank[rx] += 1

            return True

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u, v)

        




        
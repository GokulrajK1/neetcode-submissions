class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(0, len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]
        
        def union(u, v):
            pU, pV = find(u), find(v)
            if pU == pV:
                return False 

            if rank[pU] > rank[pV]:
                rank[pU] += rank[pV]
                parent[pV] = u
            else:
                rank[pV] += rank[pU]
                parent[pU] = v

            return True             
            

        def find(u):
            p = parent[u]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p 

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        




        
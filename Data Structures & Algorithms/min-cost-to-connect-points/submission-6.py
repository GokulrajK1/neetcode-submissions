class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (dist, (i, j)))

        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])

            return parent[u]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv: return False 
            if rank[ru] > rank[rv]:
                parent[rv] = ru
            elif rank[ru] < rank[rv]:
                parent[ru] = rv
            else:
                parent[rv] = ru
                rank[ru] += 1 

            return True 


        count = 0
        min_cost = 0

        while edges:
            cost, (i, j) = heapq.heappop(edges)
            if not union(i, j): continue 
            count += 1
            min_cost += cost
            if count == n - 1: break 

        return min_cost
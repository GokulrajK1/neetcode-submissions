class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [x for x in range(n)]
        rank = [1 for _ in range(n)]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return False 

            if rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
                rank[parent_u] += rank[parent_v]
            elif rank[parent_v] > rank[parent_u]:
                parent[parent_u] = parent_v
                rank[parent_v] += rank[parent_u]
            else:
                parent[parent_v] = parent_u
                rank[parent_u] += 1

            return True 

        min_heap = []

        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heapq.heappush(min_heap, (dist, (i, j)))

        print(min_heap, len(min_heap))

        count = 0 
        min_cost = 0
        while min_heap and count < n - 1:
            print("HI")
            dist, (i, j) = heapq.heappop(min_heap)
            if not union(i, j):
                continue 
            min_cost += dist 
            count += 1 

        return min_cost
                

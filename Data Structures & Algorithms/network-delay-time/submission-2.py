class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []

        for u, v, t in times:
            graph[u].append((v, t))

        dist = {k : 0}
        min_heap = [(0, k)]
        visited = set()

        while min_heap:
            d, node = heapq.heappop(min_heap)
            if node in visited: continue 
            visited.add(node)
            for i, t in graph[node]:
                if d + t > dist.get(i, float('inf')): continue 
                dist[i] = d + t 
                heapq.heappush(min_heap, (d + t, i))

        max_time = 0

        for i in range(1, n + 1):
            if i not in dist: return -1
            max_time = max(dist[i], max_time)

        return max_time 
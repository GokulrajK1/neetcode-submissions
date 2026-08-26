class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i : [] for i in range(1, n + 1)}
        for u, v, t in times:
            graph[u].append((v, t))
        
        min_heap = [(0, k)]
        dist = {i : float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        while min_heap:
            d, v = heapq.heappop(min_heap)
            print(d, v)
            for u, t in graph[v]:
                print("n", u, t)
                if d + t < dist[u]:
                    dist[u] = d + t 
                    heapq.heappush(min_heap, (dist[u], u))
            print(dist)

        max_time = max(dist.values())
        return max_time if max_time != float("inf") else -1 
            
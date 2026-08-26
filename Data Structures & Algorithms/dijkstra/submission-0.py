class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [[edge[1], edge[2]]]


        for i in range(n):
            if i not in graph:
                graph[i] = []
        
        shortest = {}

        min_heap = [[0, src]]
        while min_heap:
            weight, node = heapq.heappop(min_heap)

            if node in shortest:
                continue 

            shortest[node] = weight 

            for new_node, new_weight in graph[node]:
                heapq.heappush(min_heap, [weight + new_weight, new_node])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest



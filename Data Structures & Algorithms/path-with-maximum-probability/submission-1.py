class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        for edge, prob in zip(edges, succProb):
            graph[edge[0]] = graph.get(edge[0], []) + [[edge[1], prob]]
            graph[edge[1]] = graph.get(edge[1], []) + [[edge[0], prob]]

        for i in range(n):
            if i not in graph:
                graph[i] = []
        
        max_heap = [[-1, start_node]]

        visited = set()
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            if node in visited:
                continue
            if node == end_node:
                return abs(prob) 
            visited.add(node)
            neighbors = graph[node]
            for new_node, new_prob in neighbors:
                heapq.heappush(max_heap, [new_prob * prob, new_node])

        return 0 

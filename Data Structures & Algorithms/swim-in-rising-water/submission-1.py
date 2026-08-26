class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heights = [[float("inf")] * n for _ in range(n)]
        heights[0][0] = 0
        min_heap = [[grid[0][0], (0, 0)]]
        visited = set()
        while min_heap:
            h, (i, j) = heapq.heappop(min_heap)
            if (i, j) in visited:
                continue 
            if i == n - 1 and j == n - 1:
                return h 

            visited.add((i, j))
            
            if i - 1 >= 0:
                heapq.heappush(min_heap, [max(h, grid[i - 1][j]), (i - 1, j)])
            if i + 1 <= n - 1:
                heapq.heappush(min_heap, [max(h, grid[i + 1][j]), (i + 1, j)])
            if j - 1 >= 0:
                heapq.heappush(min_heap, [max(h, grid[i][j - 1]), (i, j - 1)])
            if j + 1 <= n - 1:
                heapq.heappush(min_heap, [max(h, grid[i][j + 1]), (i, j + 1)])
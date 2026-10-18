class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        
        dist = {(0, 0) : 0}
        min_heap = [(0, (0,0), grid[0][0])]
        visited = set()

        while min_heap:

            d, (i, j), t = heapq.heappop(min_heap)
            if (i, j) in visited: continue 
            if i == m - 1 and j == n - 1:
                return t
            visited.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= m or y >= n: continue 
                key = (grid[x][y], (x,y), max(t, grid[x][y]))
                heapq.heappush(min_heap, key)

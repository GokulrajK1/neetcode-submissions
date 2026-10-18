class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m, n = len(heights), len(heights[0])
        
        max_diffs = {(0, 0) : 0}
        min_heap = [(0, (0,0))]

        visited = set()

        while min_heap:
            diff, (i, j) = heapq.heappop(min_heap)
            if (i, j) in visited:
                continue 
            visited.add((i,j))
            max_diffs[(i, j)] = diff
            if (i, j) == (m - 1, n - 1):
                break
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= m or y >= n: continue
                if (x, y) in visited: continue 
                d = max(diff, abs(heights[i][j] - heights[x][y]))
                if d > max_diffs.get((x,y), float("inf")): continue
                key = (d, (x,y))
                heapq.heappush(min_heap, key) 

        return max_diffs[(m - 1, n - 1)]

        



                

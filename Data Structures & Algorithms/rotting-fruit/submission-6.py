class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        m, n = len(grid), len(grid[0])

        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        visited = set()

        while queue and fresh > 0:
            for i in range(len(queue)):
                i, j = queue.popleft()

                visited.add((i, j))

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    if i + dx < 0 or j + dy < 0 or i + dx >= m or j + dy >= n: continue 
                    if grid[i + dx][j + dy] == 0 or grid[i + dx][j + dy] == 2: continue 
                    if (i + dx, j + dy) in visited: continue 
                    if grid[i + dx][j + dy] == 1: fresh -= 1
                    grid[i + dx][j + dy] = 2
                    queue.append((i + dx, j + dy))

            minutes += 1

        return minutes if fresh == 0 else -1

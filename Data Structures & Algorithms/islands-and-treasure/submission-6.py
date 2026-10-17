class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append(((i,j), 0))

        visited = set()

        while queue:
            (i, j), dist = queue.popleft()

            if i < 0 or j < 0 or i >= m or j >= n: continue

            if (i, j) in visited: continue 

            if grid[i][j] == -1: continue 

            if grid[i][j] < dist: continue 

            grid[i][j] = min(dist, grid[i][j])

            visited.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                queue.append(((i + dx, j + dy), dist + 1))







class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(x, y):
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                return 0 

            if (x, y) in visited:
                return 0 

            if grid[x][y] == 0:
                return 0 

            visited.add((x, y))

            return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))

        return area

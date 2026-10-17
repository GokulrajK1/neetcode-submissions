class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 

            if grid[i][j] == "0": return 

            if (i,j) in visited: return 

            visited.add((i, j))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    count += 1

        return count



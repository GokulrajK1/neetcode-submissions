class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= r or i < 0 or j >= c or j < 0:
                return 
            if (i, j) in seen:
                return  
            if grid[i][j] == "0":
                return  
            
            seen.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        count = 0

        for i in range(r):
            for j in range(c):

                if (i, j) in seen:
                    continue

                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1 

        return count
 

             
            
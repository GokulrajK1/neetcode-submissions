class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = [(i, j)]
                should_count = False
                count = 0 
                while stack:
                    x, y = stack.pop()
                    
                    if (x, y) in seen:
                        continue 

                    if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                        continue 

                    if grid[x][y] == 0:
                        continue 

                    count += 1 

                    seen.add((x, y))

                    stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

                max_count = max(max_count, count)

        return max_count

                    



            

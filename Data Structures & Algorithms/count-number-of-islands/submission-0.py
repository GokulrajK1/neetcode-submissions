class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = [(i, j)]
                should_count = False
                while stack:
                    x, y = stack.pop()
                    
                    if (x, y) in seen:
                        continue 

                    if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                        continue 

                    if grid[x][y] == "0":
                        continue 

                    should_count = True

                    seen.add((x, y))

                    stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

                if should_count:
                    count += 1 

        return count

                    



            

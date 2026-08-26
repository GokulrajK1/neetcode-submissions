class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])
        

        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    continue 
                visited = set()
                queue = deque([(i, j, 0)])
                print(queue)
                while queue:
                    x, y, d = queue.popleft()
                    if x >= r or x < 0 or y >= c or y < 0:
                        continue 
                    if (x, y) in visited:
                        continue 
                    if grid[x][y] == -1:
                        continue 
                    
                    grid[x][y] = min(grid[x][y], d) 
                    visited.add((x,y))

                    queue.append((x + 1, y, d + 1))
                    queue.append((x - 1, y, d + 1))
                    queue.append((x, y + 1, d + 1))
                    queue.append((x, y - 1, d + 1))
                 

        


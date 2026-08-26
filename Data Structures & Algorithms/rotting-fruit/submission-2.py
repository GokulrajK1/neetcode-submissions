class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        queue = deque([(i, j) for i in range(r) for j in range(c) if grid[i][j] == 2])
        minutes = 0 
        visited = set()
        while queue:
            explored = False
            for i in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue 

                if x >= r or x < 0 or y >= c or y < 0:
                    continue 

                if grid[x][y] == 0:
                    continue 

                visited.add((x, y))

                if grid[x][y] == 1:
                    grid[x][y] = 2 

                explored = True

                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))

            if explored:
                minutes += 1 

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1 

        return minutes - 1 if minutes != 0 else 0

        

        

                
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        queue = deque()

        m, n = len(board), len(board[0])

        visited = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        queue.append((i, j))
                        visited.add((i,j))

        

        while queue:
            i, j = queue.popleft()
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= m or y >= n: continue 
                if board[x][y] == "X": continue
                if (x, y) in visited: continue 
                visited.add((x, y))
                queue.append((x, y))
                
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    board[i][j] = "X"


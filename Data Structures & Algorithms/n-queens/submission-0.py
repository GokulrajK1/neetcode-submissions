class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)] 
        free = [[0] * n for _ in range(n)]


        def pos_generate(i, j):
            positions = [(i, x) for x in range(n) if x != j] + [(x, j) for x in range(n) if x != i]
            positions += [(i - x, j - x) for x in range(n) if i - x >= 0 and j - x >= 0 and i - x != i and j - x != j]
            positions += [(i + x, j + x) for x in range(n) if i + x < n and j + x < n and i + x != i and j + x != j]
            positions += [(i - x, j + x) for x in range(n) if i - x >= 0 and j + x < n and i - x != i and j + x != j]
            positions += [(i + x, j - x) for x in range(n) if i + x < n and j - x >= 0 and i + x != i and j - x != j]
            for pos in positions:
                x, y = pos 
                free[x][y] += 1

        def pos_decr(i, j):
            positions = [(i, x) for x in range(n) if x != j] + [(x, j) for x in range(n) if x != i]
            positions += [(i - x, j - x) for x in range(n) if i - x >= 0 and j - x >= 0 and i - x != i and j - x != j]
            positions += [(i + x, j + x) for x in range(n) if i + x < n and j + x < n and i + x != i and j + x != j]
            positions += [(i - x, j + x) for x in range(n) if i - x >= 0 and j + x < n and i - x != i and j + x != j]
            positions += [(i + x, j - x) for x in range(n) if i + x < n and j - x >= 0 and i + x != i and j - x != j]
            for pos in positions:
                x, y = pos 
                if free[x][y] > 0:
                    free[x][y] -= 1
        
        def backtrack(i):
            nonlocal res, board, free
            if i == n:
                
                res.append(["".join(row) for row in board])
                return 

            for j in range(n):
                if free[i][j] == 0:
                    free[i][j] = 1 
                    board[i][j] = "Q"
                    pos_generate(i, j)
                    backtrack(i + 1)
                    
                    board[i][j] = "."
                    free[i][j] = 0
                    pos_decr(i, j)
                    
                

        backtrack(0)
        return res

                

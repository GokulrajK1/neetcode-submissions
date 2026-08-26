class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [["."] * n for _ in range(n)] 
        col = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack(i):
            nonlocal res, board
            if i == n:
                res.append(["".join(row) for row in board])
                return 

            for j in range(n):
                if j in col or (i + j) in posDiag or (i - j) in negDiag:
                    continue 
                col.add(j)
                posDiag.add(i + j)
                negDiag.add(i - j)
                board[i][j] = "Q"
                    
                backtrack(i + 1)
                col.remove(j)
                posDiag.remove(i + j)
                negDiag.remove(i - j)
                board[i][j] = "."

        backtrack(0)
        return len(res)

                

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        pos_diag = set()
        cols = set()
        neg_diag = set()
        res = []

        def backtrack(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return 

            for j in range(n):
                if j in cols or i - j in pos_diag or i + j in neg_diag:
                    continue 
                board[i][j] = "Q"
                cols.add(j)
                pos_diag.add(i - j)
                neg_diag.add(i + j)
                backtrack(i + 1)
                board[i][j] = "."
                cols.remove(j)
                pos_diag.remove(i - j)
                neg_diag.remove(i + j)

        backtrack(0)
        return res


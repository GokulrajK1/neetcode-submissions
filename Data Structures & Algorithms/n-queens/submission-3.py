class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        right_diag = set()
        left_diag = set()


        res = []
        curr = [["."] * n for _ in range(n)]

        def backtrack(i):

            if i == n:
                res.append(["".join(row) for row in curr])
                return 

            for j in range(n):
                if j in cols or (i - j) in right_diag or (i + j) in left_diag:
                    continue 

                curr[i][j] = "Q"
                cols.add(j)
                right_diag.add(i - j)
                left_diag.add(i + j)
                backtrack(i + 1)
                curr[i][j] = "."
                cols.discard(j)
                right_diag.discard(i - j)
                left_diag.discard(i + j)

        backtrack(0)

        return res



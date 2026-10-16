class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        right_diag = set()
        left_diag = set()


        count = 0
        curr = [["."] * n for _ in range(n)]

        def backtrack(i):

            nonlocal count

            if i == n:
                count += 1
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

        return count
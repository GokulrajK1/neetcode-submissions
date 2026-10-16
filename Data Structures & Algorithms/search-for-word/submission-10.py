class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])
        
        def backtrack(i, j, k, seen):
            nonlocal n, m

            if i < 0 or j < 0 or i >= n or j >= m:
                return False

            if (i, j) in seen:
                return False

            if k >= len(word):
                return False

            if board[i][j] != word[k]:
                return False 

            if k == len(word) - 1:
                return True 

            k += 1

            seen.add((i,j))
            res = backtrack(i - 1, j, k, seen) or backtrack(i + 1, j, k, seen) or backtrack(i, j - 1, k, seen) or backtrack(i, j + 1, k, seen)
            seen.discard((i,j))

            return res 

        for i in range(n):
            for j in range(m):
                seen = set()
                if backtrack(i, j, 0, seen):
                    return True

        return False 

            

            
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        w = len(word)
        
        def backtrack(i, j, s, visited):

            if s == w:
                return True

            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            if (i, j) in visited:
                return False

            if board[i][j] != word[s]:
                return False 

            visited.add((i, j))

            v = backtrack(i + 1, j, s + 1, visited) or backtrack(i - 1, j, s + 1, visited) or backtrack(i, j + 1, s + 1, visited) or backtrack(i, j - 1, s + 1, visited)

            visited.remove((i, j))
            return v


        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0, set()):
                    return True

        return False 

            
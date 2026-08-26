class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, index, visited):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False 

            if (i, j) in visited:
                return False 


            if board[i][j] != word[index]:
                return False 

            visited.add((i, j))

            if index == len(word) - 1:
                return True 

            res = dfs(i - 1, j, index + 1, visited) or dfs(i + 1, j, index + 1, visited) or dfs(i, j - 1, index + 1, visited) or dfs(i, j + 1, index + 1, visited)

            visited.remove((i,j))

            return res


        for x in range(m):
            for y in range(n):
                visited = set()
                if dfs(x, y, 0, visited):
                    return True

        return False 
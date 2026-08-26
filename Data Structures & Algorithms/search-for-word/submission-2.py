class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        width = len(board)
        height = len(board[0])
        curr = ""

        def dfs(i, j, visited):
            nonlocal board, word, curr

            if i >= width or i < 0 or j >= height or j < 0:
                return False 

            if (i, j) in visited:
                return False 

    

            curr += board[i][j]
            visited.add((i, j))

            if curr == word:
                visited.remove((i,j))
                return True 


            found = dfs(i - 1, j, visited) or dfs(i + 1, j, visited) or dfs(i, j - 1, visited) or dfs(i, j + 1, visited)
            curr = curr[:-1]
            visited.remove((i, j))
            return found
            

        for i in range(len(board)):
            for j in range(len(board[0])):
               
                visited = set()
                if dfs(i, j, visited):
                    return True

        return False
                


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
    
        visited = set()

        def dfs(i, j):
            nonlocal visited 
            if i >= r or i < 0 or j >= c or j < 0:
                return 
            if (i, j) in visited:
                return 
            if board[i][j] == "X":
                return 

            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(r):
            for j in range(c):
                if (i == 0 or j == 0 or i == r - 1 or j == c - 1) and board[i][j] == "O":
                    print("helo")
                    dfs(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and (i, j) in visited:
                    continue 
                board[i][j] = "X"

        

    

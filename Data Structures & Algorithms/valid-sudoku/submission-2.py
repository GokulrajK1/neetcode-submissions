class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        rows = [set() for _ in range(length)]
        cols = [set() for _ in range(length)]
        squares = [set() for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in rows[i]:
                    return False 
                if board[i][j] in cols[j]:
                    return False 
                square_index = (i // 3) * 3 + j // 3 
                if board[i][j] in squares[square_index]:
                    return False 

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[square_index].add(board[i][j])

        return True

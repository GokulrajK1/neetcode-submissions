class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares[3*(i // 3) + j // 3]:
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[3*(i // 3) + j // 3].add(board[i][j])


        return True

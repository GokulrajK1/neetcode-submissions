class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                value = board[i][j]
                print(value)
                if value == ".":
                    continue 
                if value in rows[i]:
              
                    return False 
                rows[i].add(value)
                print(value, i)

                if value in cols[j]:
                    print(cols[j], j)
                    print("c")
                    return False 
                cols[j].add(value)
                print(value, j)

                square_index = (i // 3) * 3 + j // 3 
                if value in squares[square_index]:
                    return False

                print(value, square_index)

                squares[square_index].add(value)

        return True 

                


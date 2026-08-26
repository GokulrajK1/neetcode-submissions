def print_matrix(matrix):
    for row in matrix:
        string = ""
        for col in row:
            string += f"{col} "
        print(string)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        print_matrix(matrix)
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    self.prefix[i][j] = self.matrix[i][j] + (self.prefix[i - 1][j] if i > 0 else 0)
                else:
                    self.prefix[i][j] = self.prefix[i][j - 1] + self.matrix[i][j] + ((self.prefix[i - 1][j] - self.prefix[i - 1][j - 1]) if i > 0 else 0 )
 
        print("_---------------------")
        print_matrix(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        print(total)
        top = 0 if row1 == 0 else self.prefix[row1 - 1][col2]
        print(top)
        left = 0 if col1 == 0 else self.prefix[row2][col1 - 1]
        print(left)
        extra = 0 if row1 == 0 or col1 == 0 else self.prefix[row1 - 1][col1 -1]
        return total - top - left + extra
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
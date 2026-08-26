class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        columns = len(matrix[0])
        self.prefix = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if i == 0 and j == 0:
                    self.prefix[i][j] = self.matrix[i][j]
                elif i == 0:
                    self.prefix[i][j] = self.matrix[i][j] + self.prefix[i][j - 1]
                elif j == 0:
                    self.prefix[i][j] = self.matrix[i][j] + self.prefix[i - 1][j]
                else:
                    self.prefix[i][j] = self.matrix[i][j] + self.prefix[i - 1][j] + self.prefix[i][j - 1] - self.prefix[i - 1][j - 1]

        self.print_matrix(self.matrix)
        print("-----------------")
        self.print_matrix(self.prefix)

                
    def print_matrix(self, matrix):
        for row in matrix:
            string = ""
            for val in row:
                string += f"{val} "
            print(string)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total = self.prefix[row2][col2]
        print(total)
        top = 0 if row1 == 0 else self.prefix[row1 - 1][col2]
        print(top)
        left = 0 if col1 == 0 else self.prefix[row2][col1 - 1]
        print(left)
        extra = 0 if col1 == 0 or row1 == 0 else self.prefix[row1 - 1][col1 - 1]
        print(extra)
        return total - top - left + extra
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
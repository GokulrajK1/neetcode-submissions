class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0] * len(self.matrix[0]) for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            running = 0
            for j in range(len(self.matrix[0])):
                running += self.matrix[i][j]
                if i == 0 and j == 0:
                    self.prefix[i][j] = self.matrix[i][j]
                elif i == 0:
                    self.prefix[i][j] = running
                elif j == 0:
                    self.prefix[i][j] = self.prefix[i - 1][j] + self.matrix[i][j]
                else:
                    self.prefix[i][j] = self.prefix[i - 1][j] + running
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = 0 if row1 == 0 else self.prefix[row1 - 1][col2]
        left = 0 if col1 == 0 else self.prefix[row2][col1 - 1]
        shared = 0 if row1 == 0 or col1 == 0 else self.prefix[row1 - 1][col1 - 1]
        total = self.prefix[row2][col2]
        return total - top - left + shared


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
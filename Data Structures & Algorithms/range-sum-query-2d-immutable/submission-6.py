class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.prefix_sum_matrix[0][0] = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    continue 
                elif i == 0:
                    self.prefix_sum_matrix[i][j] = self.prefix_sum_matrix[i][j - 1] + matrix[i][j]
                elif j == 0:
                    self.prefix_sum_matrix[i][j] = self.prefix_sum_matrix[i - 1][j] + matrix[i][j]
                else:
                    self.prefix_sum_matrix[i][j] = self.prefix_sum_matrix[i][j - 1] + self.prefix_sum_matrix[i - 1][j] + matrix[i][j] - self.prefix_sum_matrix[i - 1][j - 1]


        for row in self.prefix_sum_matrix:
            print(" ".join([str(num) for num in row]))



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum_matrix[row2][col2]
        top = 0 if row1 == 0 else self.prefix_sum_matrix[row1 - 1][col2]
        left = 0 if col1 == 0 else self.prefix_sum_matrix[row2][col1 -1]
        overlap = 0 if row1 == 0 or col1 == 0 else self.prefix_sum_matrix[row1 - 1][col1 - 1]
        return total - top - left + overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
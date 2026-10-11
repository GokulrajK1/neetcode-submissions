class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        lo = 0
        hi = n * m - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            i, j = mid // m, mid % m
            if matrix[i][j] < target:
                lo = mid + 1
            elif matrix[i][j] > target:
                hi = mid - 1
            else:
                return True

        return False
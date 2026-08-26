class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        lo = 0 
        hi = n * m - 1 
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            i = mid // m
            j = mid % m
            if target > matrix[i][j]:
                lo = mid + 1
            elif target < matrix[i][j]:
                hi = mid - 1
            else:
                return True

        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        lo = 0 
        hi = rows * cols - 1
        while lo <= hi: 
            mid = lo + (hi - lo) // 2 
            row_index, col_index = mid // cols, mid % cols 
            if target > matrix[row_index][col_index]:
                lo = mid + 1
            elif target < matrix[row_index][col_index]:
                hi = mid - 1
            else:
                return True 

        return False 
            

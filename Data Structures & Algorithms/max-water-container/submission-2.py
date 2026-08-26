class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        i = 0 
        j = n - 1
        while i < j:
            maxArea = max(maxArea, min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1 
            else:
                j -= 1 

        return maxArea
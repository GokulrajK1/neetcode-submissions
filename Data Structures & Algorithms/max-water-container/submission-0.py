class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1 
        max_amount = 0
        while i < j:
            dist = j - i
            height = min(heights[i], heights[j])
            amount = dist * height 
            if amount > max_amount:
                max_amount = amount 
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1 

        return max_amount 
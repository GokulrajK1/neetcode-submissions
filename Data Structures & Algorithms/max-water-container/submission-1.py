class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1 
        max_area = 0
        while l < r:
            dist = r - l 
            if heights[l] > heights[r]:
                min_height = heights[r]
                r -= 1
            else:
                min_height = heights[l]
                l += 1
            area = min_height * dist 
            if area > max_area:
                max_area = area 

        return max_area
            
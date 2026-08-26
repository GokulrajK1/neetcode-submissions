class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        area = 0
        while l < r:
            if max_left < max_right:
                area += min(max_left, max_right) - height[l]
                l += 1 
                max_left = max(max_left, height[l])
            else:
                area += min(max_left, max_right) - height[r]
                r -= 1 
                max_right = max(max_right, height[r])

        return area
            
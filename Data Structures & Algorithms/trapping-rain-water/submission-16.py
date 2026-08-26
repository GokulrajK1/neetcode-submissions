class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = height[0]
        max_right = height[n - 1]
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            if max_left < max_right:
                max_area += max_left - height[i]
                i += 1 
                max_left = max(max_left, height[i])
            else:
                
                max_area += max_right - height[j]
                j -= 1
                max_right = max(max_right, height[j])

        return max_area

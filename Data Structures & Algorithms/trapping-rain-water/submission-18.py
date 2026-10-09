class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_left = height[i]
        max_right = height[j]
        area = 0
        while i < j:
            if max_left < max_right:
                area += max_left - height[i]
                i += 1
                max_left = max(height[i], max_left)
                
            else:
                area += max_right - height[j]
                j -= 1
                max_right = max(height[j], max_right) 
                

        return area
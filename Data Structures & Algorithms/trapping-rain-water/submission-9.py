class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        max_left = height[i]
        max_right = height[j]
        result = 0
        while i <= j:
            if max_left < max_right:
                max_left = max(height[i], max_left)
                result += max_left - height[i]
                i += 1
            else:
                max_right = max(height[j], max_right)
                result += max_right - height[j]
                j -= 1 

        return result
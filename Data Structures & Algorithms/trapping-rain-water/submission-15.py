class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        
        maxL = height[i]
        maxR = height[j]

        area = 0 

        while i < j:
            if maxL < maxR:
                area += maxL - height[i]
                i += 1
                maxL = max(maxL, height[i])
            else:
                area += maxR - height[j]
                j -= 1
                maxR = max(maxR, height[j])

        return area



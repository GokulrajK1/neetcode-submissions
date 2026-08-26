class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        while i < j and height[i] == 0:
            i += 1
        while i < j and height[j] == 0:
            j -= 1

        area = 0 
        curr_height = min(height[i], height[j])
        while i < j:
            min_height = min(height[i], height[j])
            if min_height > curr_height:
                curr_height = min_height 
            area += curr_height - min_height

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1 

        return area 



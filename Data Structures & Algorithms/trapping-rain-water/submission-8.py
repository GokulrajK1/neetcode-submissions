class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        result = 0 
        left_max, right_max = height[l], height[r]
        while l <= r:
            if left_max < right_max:
                left_max = max(left_max, height[l])
                result += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                result += right_max - height[r]
                r -= 1 
        return result 
        # l = 0 
        # n = len(height)
        # while l < n and height[l] == 0:
        #     l += 1 
        
        # r = l + 1
        
        # total_area = 0
        # while l < r and l < n and r < n:
        #     curr_height = height[l]
        #     to_add = 0
        #     higher_found = False 
        #     unchanged = False
        #     second_highest_area = 0
        #     second_highest_height = 0 
        #     second_highest_index = 0
        #     while r < n:
                
        #         if height[r] >= curr_height:
        #             higher_found = True
        #             break
        #         if height[r] > second_highest_height:
        #             second_highest_height = height[r]
        #             second_highest_index = r 
        #             second_highest_area = to_add
        #             unchanged = True

        #         to_add += curr_height - height[r]
        #         r += 1 

        #     if higher_found:
        #         total_area += to_add
        #         l = r 
        #         r += 1 
            
        #     else:
                
        #         if not unchanged:
        #             break
        #         dist = second_highest_index - l - 1
        #         second_highest_area -= (dist * (curr_height - second_highest_height))
        #         total_area += second_highest_area 
        #         l = second_highest_index
        #         r = l + 1 
               

        # return total_area




                
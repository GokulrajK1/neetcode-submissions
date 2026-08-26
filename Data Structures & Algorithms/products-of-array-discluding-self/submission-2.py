class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        index = 0 
        total_product = 1 
        for i, num in enumerate(nums):
            if num == 0:
                index = i 
                count += 1 
            else:
                total_product *= num 

        if count > 1:
            return [0] * len(nums)

        elif count == 1:
            output = [0] * len(nums)
            output[index] = total_product 
            return output

        else:
            output = []
            for num in nums:
                output.append(total_product // num)
            return output
        
    
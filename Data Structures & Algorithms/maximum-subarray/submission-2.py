class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        max_sum = nums[0]
        for num in nums:
            if prefix < 0:
                prefix = num
            else:
                prefix += num 
            
            if prefix > max_sum:
                max_sum = prefix

            print(prefix, num)

        return max_sum 

            
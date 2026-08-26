class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0
        for n in nums:
            if n == majority:
                count += 1 
            else:
                count -= 1
                if count == 0:
                    majority = n
                    count += 1


        return majority
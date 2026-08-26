class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_element = nums[0]
        for num in nums:
            if num == majority_element:
                count += 1
            elif count == 0 and num != majority_element:
                count += 1
                majority_element = num
            else:
                count -= 1

        return majority_element
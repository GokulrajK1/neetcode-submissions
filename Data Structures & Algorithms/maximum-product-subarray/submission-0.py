class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]
        for num in nums:
            temp = currMax * num
            currMax = max(temp, num, currMin * num)
            currMin = min(temp, num, currMin * num)
            res = max(currMax, res)

        return res





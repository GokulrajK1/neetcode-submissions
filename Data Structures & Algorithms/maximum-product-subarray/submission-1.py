class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = nums[0]

        for num in nums:
            temp = currMax * num
            currMax = max(num, temp, num * currMin)
            currMin = min(num, temp, num * currMin)
            res = max(currMax, res)

        return res


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        total = 0
        length = float("inf")
        for j in range(len(nums)):

            total += nums[j]

            while i <= j and total >= target:
                print(i, j)
                length = min(length, j - i + 1)
                total -= nums[i]
                i += 1

            

        return length if length != float("inf") else 0


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            index = abs(nums[i]) - 1
            if index < 0 or index > n - 1:
                continue
            if nums[index] == 0:
                nums[index] = -(n + 1)
            elif nums[index] > 0:
                nums[index] = -nums[index]

        print(nums)

        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1
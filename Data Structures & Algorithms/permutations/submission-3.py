class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(numbers):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for i in range(len(numbers)):
                curr.append(numbers[i])
                backtrack(numbers[:i] + numbers[i+1:])
                curr.pop()

        backtrack(nums)
        return res
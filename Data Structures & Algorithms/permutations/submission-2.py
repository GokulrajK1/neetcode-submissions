class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        curr = []
        
        def backtrack(numbers):
            nonlocal n, res, curr

            if len(curr) == n:
                res.append(curr.copy())

            for i, number in enumerate(numbers):
                curr.append(number)
                backtrack(numbers[:i] + numbers[i + 1:])
                curr.pop()
        
        backtrack(nums)
        return res 


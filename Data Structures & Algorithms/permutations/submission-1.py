class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        
        def backtrack(curr, numbers):
            nonlocal n, res

            for i, number in enumerate(numbers):
                new_curr = curr.copy()
                new_curr.append(number)
                if len(new_curr) == n:
                    res.append(new_curr)
                else:
                    backtrack(new_curr, numbers[:i] + numbers[i + 1:])

        curr = []
        backtrack(curr, nums)
        return res 


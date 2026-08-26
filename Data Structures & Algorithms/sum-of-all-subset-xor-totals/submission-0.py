class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        total = 0 
        
        def backtrack(sum, i):

            nonlocal total 

            if i == len(nums):
                total += sum 
                return 

            backtrack(sum ^ nums[i], i + 1)
            backtrack(sum, i + 1)


        backtrack(0, 0)

        return total
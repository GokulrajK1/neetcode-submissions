class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * n 
        for i in range(n - 1):
            results[i + 1] = results[i] * nums[i]

        suffix = 1 
        for j in range(n - 1, -1, -1):
            results[j] *= suffix
            suffix *= nums[j]

        return results

        


        
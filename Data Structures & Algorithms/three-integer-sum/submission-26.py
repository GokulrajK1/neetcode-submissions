class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        target = 0 
        res = []
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            j = i + 1
            k = n - 1 
            while j < k:
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]]) 
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    k -= 1
        return res
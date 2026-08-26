class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        print(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            j = i + 1 
            k = n - 1 
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1 
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                     
        return result 
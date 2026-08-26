class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        result_set = set()
        print(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            j = i + 1 
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1 
                elif nums[j] + nums[k] < target:
                    j += 1 
                else:
                    if (nums[i], nums[j], nums[k]) in result_set:
                        j += 1
                        k -= 1
                        continue
                    result_set.add((nums[i], nums[j], nums[k]))
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1
                    
        return result
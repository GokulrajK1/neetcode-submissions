class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 
                k = j + 1 
                l = n - 1
                x = target - nums[i] - nums[j] 
                while k < l:
                    if nums[k] + nums[l] > x:
                        l -= 1 
                    elif nums[k] + nums[l] < x:
                        k += 1 
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1 
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1 

        return result

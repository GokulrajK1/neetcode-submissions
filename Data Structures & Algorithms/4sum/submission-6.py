class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 

                k = j + 1
                l = n - 1 
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1 
                        l -= 1
                        while k < n and nums[k] == nums[k - 1]:
                            k += 1

        return res

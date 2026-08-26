class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        print(nums)
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 

            for j in range(i + 1, n):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue 

                new_target = target - nums[i] - nums[j]
                k = j + 1
                l = n - 1
                while k < l:
                    if nums[k] + nums[l] > new_target:
                        l -= 1 
                    elif nums[k] + nums[l] < new_target:
                        k += 1 
                    else:
                        print(i, j , k, l)
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1 
                        l -= 1
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1 
                        
        return result 

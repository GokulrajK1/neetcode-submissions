class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            j = i + 1 
            k = n - 1 
            print(i)
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1 
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1 
                else:
                    if k < n - 1 and nums[j] == nums[j - 1] and nums[k] == nums[k + 1]:
                        j += 1 
                        k -= 1
                        continue
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1


            
        return res
                    

            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            j = i + 1 
            k = len(nums) - 1 
            
            while j < k:
                
                if nums[i] + nums[j] + nums[k] > 0:
                    
                    k -= 1 
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    l = j + 1 
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1 

                    j = l 

        return res

        

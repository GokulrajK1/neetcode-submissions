class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0 
        unique = set()
        for j in range(len(nums)):
            if j - i > k:
                unique.remove(nums[i])
                i += 1 
            if nums[j] in unique:
                return True
            unique.add(nums[j])
        
        return False
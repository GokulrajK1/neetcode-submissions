class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        n = len(nums)
        l = 0 
        r = 0 
        while r < n:
            if r - l > k:
                seen.remove(nums[l])
                l += 1 
                continue 
            if nums[r] in seen:
                return True 
            seen.add(nums[r])
            r += 1 

        return False 
            
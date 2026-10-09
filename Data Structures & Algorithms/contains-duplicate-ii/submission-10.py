class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        n = len(nums)
        nearby = set()
        for j in range(n):
            if abs(i - j) > k:
                nearby.remove(nums[i])
                i += 1

            if nums[j] in nearby: return True 
            nearby.add(nums[j])

        return False 
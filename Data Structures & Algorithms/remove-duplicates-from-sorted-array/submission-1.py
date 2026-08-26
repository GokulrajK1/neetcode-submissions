class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                j = i 
                while nums[j] in seen:
                    j += 1 
                    if j >= n:
                        return i 
                nums[i] = nums[j]
                seen.add(nums[i])

        return n

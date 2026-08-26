class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0 
        result = 0
        prefix_counts = {}
        for num in nums:
            prefix += num 
             
            if prefix == k:
                result += 1 
            if prefix - k in prefix_counts:
                result += prefix_counts[prefix - k]

            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

        return result
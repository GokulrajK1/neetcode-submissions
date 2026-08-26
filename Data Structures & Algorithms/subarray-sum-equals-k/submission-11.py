class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {}
        prefix = 0
        res = 0 
        for num in nums:
            prefix += num

            if prefix == k:
                res += 1 
            
            
            res += prefixes.get(prefix - k, 0)
            prefixes[prefix] = prefixes.get(prefix, 0) + 1

           

        return res 

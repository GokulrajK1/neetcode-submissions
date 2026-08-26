class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix_counts = {}
        count = 0
        for num in nums:
            total += num 
            print("total")
            print(total)
            if total == k:
                count += 1 
            
                
            if total - k in prefix_counts:
                print("prefix")
                count += prefix_counts[total - k]
            prefix_counts[total] = prefix_counts.get(total, 0) + 1 
            print("count")
            print(count)

        return count 


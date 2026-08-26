class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if len(counts) < 2: 
                continue 
            new_counts = {}
            for n, c in counts.items():
                if c > 1:
                    new_counts[n] = c - 1

            counts = new_counts 
        if len(counts) > 2:
            return "hello"
        for n in counts:
            if nums.count(n) > (len(nums) // 2):
                return n
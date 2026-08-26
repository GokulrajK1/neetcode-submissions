class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 

            if len(counts) <= 2:
                continue 

            for num, count in counts.items():
                if count > 1:
                    counts[num] -= 1 

        res = []
        for num in counts.keys():
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res
        
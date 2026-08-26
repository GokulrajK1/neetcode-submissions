class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # size = len(nums) // 3 
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1 
        # result = []
        # for num, count in counts.items():
        #     if count > size:
        #         result.append(num)

        # return result

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
            if len(counts) <= 2:
                continue 
            new_counts = {}
            for n, c in counts.items():
                if c > 1:
                    new_counts[n] = c - 1
            counts = new_counts

        result = []

        for n in counts:
            if nums.count(n) > len(nums) // 3:
                result.append(n)

        return result
            
        

        
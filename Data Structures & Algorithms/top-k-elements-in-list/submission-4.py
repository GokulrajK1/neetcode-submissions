class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1 
        
        frequencies = {}
        for num, count in counts.items():
            frequencies[count] = frequencies.get(count, []) + [num]

        max_count = max(frequencies.keys())
        res = []

        for i in range(max_count, -1, -1):
            if i in frequencies:
                res += frequencies[i]
                if len(res) == k:
                    return res

        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            count = counts.get(num, 0) + 1
            counts[num] = count

        frequencies = {}
        for num, count in counts.items():
            numbers = frequencies.get(count, [])
            numbers.append(num)
            frequencies[count] = numbers 

        res = []
        for frequency in range(len(nums), 0, -1):
            if frequency not in frequencies:
                continue 

            res.extend(frequencies[frequency])

            if len(res) >= k:
                return res[:k]


        

        
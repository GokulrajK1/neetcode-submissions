class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 

        frequencies = {}
        for num, count in counts.items():
            nums_list = frequencies.get(count, [])
            nums_list.append(num)
            frequencies[count] = nums_list 

        result = []
        for frequency in range(len(nums), 0, -1):
            if frequency in frequencies:
                result += frequencies[frequency]
                if len(result) == k:
                    break

        return result
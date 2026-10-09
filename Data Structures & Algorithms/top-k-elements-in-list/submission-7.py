class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = {}
        for num, val in count.items():
            numbers = freq.get(val, [])
            numbers.append(num)
            freq[val] = numbers

        ans = []

        for f in range(len(nums), -1, -1):
            if f not in freq:
                continue 
            ans += freq[f]
            if len(ans) >= k:
                return ans[:k]
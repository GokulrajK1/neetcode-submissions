class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] =  1 + counts.get(num, 0)
        
        frequencies = [[] for i in range(len(nums) + 1)]
        for key, value in counts.items():
            frequencies[value].append(key)
        
        answer = []
        count = 0
        for frequency in frequencies[::-1]:
            if frequency:
                answer += frequency
                count += len(frequency)
                
            if count == k:
                return answer 
        

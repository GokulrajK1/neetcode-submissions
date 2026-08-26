class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a counts dict to count the number of times each element appears
        # create frequncies dict to group elements that appear the same number of times together
        # the upper bound for any element's count is the lenght of the list so we will just iterate
        # through until and add elements to our result until we reach k elements 

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
        
        frequencies = {} 
        for num, count in counts.items():
            if count not in frequencies:
                frequencies[count] = []
            frequencies[count].append(num)
      
        res = [] 
        for frequency in range(len(nums), -1, -1):
            if frequency in frequencies:
                res.extend(frequencies[frequency])
                if len(res) >= k:
                    return res[:k]
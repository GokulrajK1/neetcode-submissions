import math
import heapq 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
        
        left = 0 
        heap = []
        res = []
        for right in range(len(nums)):
            heapq.heappush(heap, -nums[right])
            if right - left + 1 == k:
                res.append(-heap[0])
                counts[nums[left]] -= 1
                while heap and counts[-heap[0]] == 0:
                    heapq.heappop(heap)
                left += 1 
                

        return res 
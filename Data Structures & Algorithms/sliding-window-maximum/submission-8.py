import math
import heapq 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        heap = []
        res = []
        counts = {}
        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            heapq.heappush(heap, -nums[right])
            if right - left + 1 == k:
                while heap and counts[-heap[0]] == 0:
                    heapq.heappop(heap)
                res.append(-heap[0])
                counts[nums[left]] -= 1
                left += 1 
                

        return res 
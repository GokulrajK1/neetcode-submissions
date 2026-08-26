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
                print(nums[right])
                print(heap)
                print(-heap[0])
                res.append(-heap[0])

                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    while heap and nums[left] == -heap[0]:
                        heapq.heappop(heap)
                else:
                    if nums[left] == -heap[0]:
                        heapq.heappop(heap)
                left += 1 
                print(heap)
                print("------------------")

        return res 
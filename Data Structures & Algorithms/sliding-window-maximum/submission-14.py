class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        left = 0 
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()
                
            
            if right + 1 >= k:
                res.append(nums[queue[0]])

                left += 1

        return res
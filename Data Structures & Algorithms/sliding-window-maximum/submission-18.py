class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0 
        res = []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i - l + 1 == k:
                res.append(nums[queue[0]])
                l += 1 
                if l > queue[0]:
                    queue.popleft()

        return res

            
                


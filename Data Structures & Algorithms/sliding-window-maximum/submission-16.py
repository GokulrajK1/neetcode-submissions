class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        queue = deque()
        res = []
        for j in range(len(nums)):
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)

            if i > queue[0]:
                queue.popleft()

            if j + 1 >= k:
                res.append(nums[queue[0]])
                i += 1 

        return res

            

            


            

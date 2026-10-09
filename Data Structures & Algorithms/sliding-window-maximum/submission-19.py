class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        i = 0
        res = []
        for j in range(len(nums)):
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()

            queue.append(j)

            if j - i + 1 == k:
                res.append(nums[queue[0]])
                i += 1 
                if i > queue[0]:
                    queue.popleft()

        return res
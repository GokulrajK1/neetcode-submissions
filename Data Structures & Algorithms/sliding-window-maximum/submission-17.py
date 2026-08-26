class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0
        n = len(nums)
        res = []
        for r in range(n):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            if r - l + 1 == k:
                res.append(nums[queue[0]])
                l += 1 
                if l > queue[0]:
                    queue.popleft()

        return res
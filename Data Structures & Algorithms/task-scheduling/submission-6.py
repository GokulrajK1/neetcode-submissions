class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        nums = list(-x for x in counts.values())
        heapq.heapify(nums)
        queue = deque()

        t = 0 

        while nums or queue:
            while queue and queue[0][0] <= t:
                time, task = queue.popleft()
                heapq.heappush(nums, task)
            
            if not nums:
                t += 1
            
                continue 

            task = heapq.heappop(nums)
            task += 1 
            if task != 0:
                queue.append((t + n + 1, task))
            t += 1 

        return t


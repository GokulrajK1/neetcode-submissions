class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1 

        tasks_pending = []
    
        for task, count in counts.items():
            heapq.heappush(tasks_pending, (-count, task))

        cooldown = deque()
    

        time = 0
        while tasks_pending or cooldown:
            while cooldown and cooldown[0][0] == time:
                _, count, task = cooldown.popleft()
                heapq.heappush(tasks_pending, (count, task))

            if tasks_pending:
                count, task = heapq.heappop(tasks_pending)
                count += 1 
                if count != 0:
                    cooldown.append((time + n + 1, count, task))
            time += 1

        return time 

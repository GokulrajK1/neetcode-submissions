class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        min_heap = []
        for task, count in counts.items():
            min_heap.append(-count)

        heapq.heapify(min_heap)

        queue = deque([])
        time = 0 
        cycles = 0 

        while min_heap or queue:

            while queue and queue[0][1] <= time:
                task_count, _ = queue.popleft()
                heapq.heappush(min_heap, task_count)

            if not min_heap:
                time += 1
                cycles += 1 
                continue

            task_count = heapq.heappop(min_heap)
            task_count += 1

            if task_count < 0:
                queue.append((task_count, time + n + 1))
                
            cycles += 1
            time += 1 

        return cycles

        
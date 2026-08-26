class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1 

        counts = [-val for _, val in counts.items()]
        heapq.heapify(counts)

        queue = deque()

        time = 0 

        print(counts)

        while queue or counts:
            time += 1 
            if counts: 
                count = heapq.heappop(counts)
                print(count)
                count += 1 
                if count < 0:
                    queue.append((count, time + n))

            while queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(counts, count)

            
        return time
                 




        

        


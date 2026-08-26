class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i, task in enumerate(tasks):
            task.append(i)

        tasks = sorted(tasks, key=lambda x : x[0])
        minHeap = []

        res = []

        time = tasks[0][0]
        i = 0
        while i < len(tasks) or minHeap:
            
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][0], tasks[i][2]))
                i += 1

            if minHeap:
                task = heapq.heappop(minHeap)
                res.append(task[2])
                time += task[0]
                print(time, task)
            else:
                time += 1 

        return res

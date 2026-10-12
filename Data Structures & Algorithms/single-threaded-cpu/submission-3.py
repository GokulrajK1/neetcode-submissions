class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = [(enqueue_time, i, processing_time) for i, (enqueue_time, processing_time) in enumerate(tasks)]
        heapq.heapify(t)
        time = t[0][0]
        res = []
        to_process = []
        while t or to_process:
            while t and time >= t[0][0]:
                _, i, processing_time = heapq.heappop(t)
                heapq.heappush(to_process, (processing_time, i))

            if not to_process:
                time = t[0][0]
                continue
            
            processing_time, i = heapq.heappop(to_process)
            res.append(i)
            time += processing_time 

        return res
            



            
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        free = []
        count = [0] * n 

        for i in range(n):
            heapq.heappush(free, (0, i))

        for start, end in meetings:

            while free and free[0][0] < start:

                end_time, room = heapq.heappop(free)
                heapq.heappush(free, (start, room))

            end_time, room = heapq.heappop(free)
            heapq.heappush(free, (end_time + (end - start), room))
            count[room] += 1 

        return count.index(max(count))




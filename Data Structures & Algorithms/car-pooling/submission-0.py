class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        trips = sorted(trips, key=lambda x : x[1])
        curr = 0 
        for trip in trips:
            passengers, f, to = trip 
            while minHeap and minHeap[0][0] <= f:
                t, p = heapq.heappop(minHeap)
                curr -= p 
            curr += passengers 
            if curr > capacity:
                return False 
            heapq.heappush(minHeap, (to, passengers))

        return True 


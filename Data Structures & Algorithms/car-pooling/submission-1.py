class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for number, src, dst in trips:
            heapq.heappush(heap, (src, number))
            heapq.heappush(heap, (dst, -number))

        size = 0
        while heap:
            _, number = heapq.heappop(heap)
            size += number 
            if size > capacity:
                return False

        return True


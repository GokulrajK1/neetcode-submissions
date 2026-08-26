import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            heapq.heappush(maxHeap, [-math.sqrt(point[0] * point[0] + point[1] * point[1]), point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [x[1] for x in maxHeap]
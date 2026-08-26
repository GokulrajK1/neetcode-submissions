class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for x, y in points:
            heapq.heappush(closest, (-math.sqrt(x*x + y*y), (x, y)))
            if len(closest) > k:
                heapq.heappop(closest)

        return [point for _, point in closest]
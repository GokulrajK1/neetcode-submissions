class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(math.sqrt((x*x) + (y*y)), (x, y)) for x, y in points]
        heapq.heapify(dist)
        res = []
        for _ in range(k):
            if not dist:
                continue

            _, point = heapq.heappop(dist)
            res.append(point)

        return res
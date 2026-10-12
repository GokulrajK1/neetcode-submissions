class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        heapq.heapify(distances)
        res = []
        while distances and len(res) < k:
            res.append(heapq.heappop(distances)[1])

        return res
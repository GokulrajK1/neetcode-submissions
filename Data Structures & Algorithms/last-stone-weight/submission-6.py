class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if abs(x) != abs(y):
                heapq.heappush(stones, -abs(x - y))

        return 0 if len(stones) == 0 else -stones[0]
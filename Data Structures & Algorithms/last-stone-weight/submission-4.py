class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:

            x, y = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            print(x, y)
            if x != y:
                heapq.heappush(stones, abs(x - y) * -1)

        return 0 if not stones else abs(stones[0])
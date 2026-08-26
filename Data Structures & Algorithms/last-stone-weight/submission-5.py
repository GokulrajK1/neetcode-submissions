class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = [-stone for stone in stones]
        heapq.heapify(array)
        while len(array) > 1:
            stone1, stone2 = -heapq.heappop(array), -heapq.heappop(array)
            if stone1 != stone2:
                heapq.heappush(array, -abs(stone1 - stone2))

        return -array[0] if array else 0
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k 
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(nums)

        print(self.heap)

    def add(self, val: int) -> int:
        if not self.heap or len(self.heap) < self.k:
            heapq.heappush(self.heap, val) 

        elif self.heap and val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]

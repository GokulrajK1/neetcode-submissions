class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -num)
        heapq.heappush(self.larger, -heapq.heappop(self.smaller))
        if len(self.larger) > len(self.smaller):
            heapq.heappush(self.smaller, -heapq.heappop(self.larger))

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]

        return (-self.smaller[0] + self.larger[0]) / 2
        
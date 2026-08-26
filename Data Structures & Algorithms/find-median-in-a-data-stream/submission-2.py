class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        self.smallest = float("inf")
        self.largest = float("-inf")

    def addNum(self, num: int) -> None:
        if not self.smaller and not self.larger:
            self.smaller.append(-num)
            self.smallest = num 
            return
            
        if not self.larger:
            self.larger.append(num)
            self.largest = num 

            if self.largest < self.smallest:
                self.smallest, self.largest = self.largest, self.smallest
                self.smaller = [-self.smallest]
                self.larger = [self.largest]

            return

        if num >= -(self.smaller[0]) and num <= self.larger[0]:
            if len(self.smaller) <= len(self.larger):
                heapq.heappush(self.smaller, -num)
            else:
                heapq.heappush(self.larger, num)

        elif num < self.smallest: 
            if len(self.smaller) <= len(self.larger):
                heapq.heappush(self.smaller, -num)
                self.smallest = num 
            else:
                self.smallest = num 
                largestSmall = -heapq.heappop(self.smaller)
                heapq.heappush(self.smaller, -num)
                heapq.heappush(self.larger, largestSmall)

        elif num > self.largest:
            if len(self.larger) <= len(self.smaller):
                heapq.heappush(self.larger, num)
                self.largest = num 
            else:
                self.largest = num 
                smallestLarge = heapq.heappop(self.larger)
                heapq.heappush(self.larger, num)
                heapq.heappush(self.smaller, -smallestLarge)

        elif num >= self.smallest and num < -(self.smaller[0]):
            if len(self.smaller) <= len(self.larger):
                heapq.heappush(self.smaller, -num)
            else:
                largestSmall = -heapq.heappop(self.smaller)
                heapq.heappush(self.smaller, -num)
                heapq.heappush(self.larger, largestSmall)
        
        else:
            if len(self.larger) <= len(self.smaller):
                heapq.heappush(self.larger, num)
            else:
                smallestLarge = heapq.heappop(self.larger)
                heapq.heappush(self.larger, num)
                heapq.heappush(self.smaller, -smallestLarge)

        print(self.smallest, self.largest)
        print(self.smaller)
        print(self.larger)
        

    def findMedian(self) -> float:
        if self.smaller and not self.larger:
            return -self.smaller[0]

        if self.larger and not self.smaller:
            return self.larger[0]

        if len(self.larger) == len(self.smaller):
            return (self.larger[0] + -(self.smaller[0])) / 2

        else:
            if len(self.smaller) < len(self.larger):
                return self.larger[0]
            else:
                return -self.smaller[0]
        
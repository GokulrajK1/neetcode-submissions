class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        vals = [a, b, c]
        first = [(-a, "a"), (-b, "b"), (-c, "c")]
        minHeap = []
        for count, letter in first:
            if count < 0:
                minHeap.append((count, letter))
    
        heapq.heapify(minHeap)
        queue = deque()
        res = ""

        print(minHeap)

        usage = {"a" : 0, "b" : 0, "c" : 0}

        time = 0

        while minHeap or queue: 

            time += 1 

            if minHeap:
                count, letter = heapq.heappop(minHeap)
                print(count, letter)
                print(minHeap)
                if len(res) > 1:
                    if res[-1] != letter or res[-2] != letter:
                        res += letter
                else:
                    res += letter 
                print(res)
                usage[letter] += 1 
                print(usage)
                count += 1 
                if count < 0 and usage[letter] == 2:
                    print("reset")
                    queue.append((count, letter, time + 1))
                    usage[letter] = 0 
                elif count < 0 and usage[letter] < 2:
                    heapq.heappush(minHeap, (count, letter))

            while queue and queue[0][2] <= time:
                count, letter, _ = queue.popleft()
                heapq.heappush(minHeap, (count, letter))

        return res




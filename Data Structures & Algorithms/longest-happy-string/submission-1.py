class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [(-x, letter) for x, letter in zip([a, b, c], ["a", "b", "c"]) if x > 0]
        queue = deque()
        time = 0 
        res = []
        heapq.heapify(max_heap)
        print(max_heap)
        while max_heap or queue:
            while queue and queue[0][0] <= time:
                _, count, letter = queue.popleft()
                heapq.heappush(max_heap, (count, letter))

            if not max_heap:
                return "".join(res)

            count, letter = heapq.heappop(max_heap)
           
            res.append(letter)
            count += 1 
            if count < 0:
                if len(res) > 1 and res[-2] == letter:
                    queue.append((time + 2, count, letter))

                else:
                    queue.append((time + 1, count, letter))

            time += 1 

        return "".join(res)

            
        
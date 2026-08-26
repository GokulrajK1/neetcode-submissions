class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1 

        counts = [(-count, letter) for letter, count in counts.items()]
        heapq.heapify(counts)

        # print(counts)

        queue = deque()
        res = ""

        time = 0

        while counts or queue:

            time += 1 

            if counts:
                print(res)
                print(counts)
                count, letter = heapq.heappop(counts)
                count += 1 
                if res and res[-1] == letter:
                    print("hello")
                    return ""
                res += letter 
                if count < 0:
                    queue.append((count, letter, time + 1))
            
            while queue and queue[0][2] <= time:
                char = queue.popleft()
                heapq.heappush(counts, (char[0], char[1]))

        return res 

            



            


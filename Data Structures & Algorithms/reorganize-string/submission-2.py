class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) - 1

        max_heap = [(count, letter) for letter, count in counts.items()]
        buffer = deque()
        i = 0 
        res = []
        while max_heap or buffer:
            while buffer and buffer[0][0] % 2 == i % 2:
                _, count, letter = buffer.popleft()
                heapq.heappush(max_heap, (count, letter))

            if max_heap:
                count, letter = heapq.heappop(max_heap)
            else:
                return ""
            if len(res) > 0 and res[-1] == letter:
                return ""
            res.append(letter)
            count += 1
            if count < 0:
                buffer.append((i, count, letter))
            i += 1 

        return "".join(res)

        
                


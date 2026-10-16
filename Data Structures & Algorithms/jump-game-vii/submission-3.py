class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        queue.append(0)
        farthest = 0

        while queue:
            index = queue.popleft()
            if index == len(s) - 1:
                return True
            start = max(index + minJump, farthest + 1)
            end = min(index + maxJump, len(s) - 1)
            for i in range(start, end + 1):
                if s[i] == "1": continue 
                queue.append(i)

            farthest = max(farthest, end)

        return False

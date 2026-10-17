class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        queue = deque()
        queue.append(("0000", 0))

        deads = set(deadends)

        if "0000" in deads: return -1

        visited = set(["0000"])

        while queue: 
            lock, dist = queue.popleft()
            if lock == target:
                return dist 
            for i in range(8):
                inc = 1 if i < 4 else -1
                new_lock = lock[:i % 4] + str((int(lock[i % 4]) + inc) % 10) + lock[(i % 4)+1:]
                if new_lock in visited: continue 
                if new_lock in deads: continue 
                visited.add(new_lock)
                queue.append((new_lock, dist + 1))

        return -1
                
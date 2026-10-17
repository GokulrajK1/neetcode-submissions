class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        delta = [0] * n 
        for src, dst in trust:
            delta[src - 1] -= 1
            delta[dst - 1] += 1

        for i, d in enumerate(delta):
            if d == n - 1: return i + 1

        return -1
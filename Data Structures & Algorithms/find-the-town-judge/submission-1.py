class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        res = [False] * n
        trust_count = [0] * n 

        for a, b in trust:
            trust_count[b - 1] += 1
            res[a - 1] = True

        for i, p in enumerate(res):
            if not p and trust_count[i] == n - 1:
                return i + 1

        return -1
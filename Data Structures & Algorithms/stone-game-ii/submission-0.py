class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        memo = {}

        def backtrack(i, is_alice, M):
            if (i, is_alice, M) in memo: return memo[(i, is_alice, M)]
            if i == n: return 0

            res = 0 if is_alice else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > n: break 
                total += piles[i + X - 1]
                if is_alice:
                    res = max(res, total + backtrack(i + X, not is_alice, max(M, X)))
                else:
                    res = min(res, backtrack(i + X, not is_alice, max(M, X)))

            memo[(i, is_alice, M)] = res

            return res

        return backtrack(0, True, 1)


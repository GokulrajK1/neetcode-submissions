class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        
        def backtrack(total): 
            if total in memo: return memo[total]
            if total == 0: return 0 

            min_count = float("inf")

            for coin in coins:
                if total - coin < 0: continue 
                min_count = min(min_count, 1 + backtrack(total - coin))

            memo[total] = min_count

            return min_count

        res = backtrack(amount)
        return res if res != float("inf") else -1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        
        def backtrack(i, remaining, memo):

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            if remaining == 0:
                return 1 

            if remaining < 0:
                return 0 

            if i == n:
                return 0 

            memo[(i, remaining - coins[i])] = backtrack(i, remaining - coins[i], memo) 
            memo[(i + 1, remaining)] = backtrack(i + 1, remaining, memo)

            return memo[(i, remaining - coins[i])] + memo[(i + 1, remaining)]

        return backtrack(0, amount, {})
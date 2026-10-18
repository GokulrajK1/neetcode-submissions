class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        n = len(stones)
        
        total = sum(stones)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(stones)):
            for amount in range(target, 0, -1):
                if amount < stones[i]: continue 
                if dp[amount - stones[i]]:
                    dp[amount] = True

        for i in range(target, -1, -1):
            if dp[i]:
                return total - i * 2
        return 0


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0 : 1, 1 : 1}
        for i in range(2, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]
        return memo[n]

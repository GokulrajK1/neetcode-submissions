class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: 
            return False 

        side = total // 4

        if max(matchsticks) > side:
            return False 

        piles = [0] * 4

        ans = False 

        def backtrack(i):

            nonlocal ans 

            if i == len(matchsticks):
                if piles[0] == piles[1] == piles[2] == piles[3]:
                    ans = True 

                return 

            for j in range(len(piles)):
                if piles[j] + matchsticks[i] > side:
                    continue 
                
                piles[j] += matchsticks[i]
                backtrack(i + 1)
                piles[j] -= matchsticks[i]

        backtrack(0)

        return ans
                
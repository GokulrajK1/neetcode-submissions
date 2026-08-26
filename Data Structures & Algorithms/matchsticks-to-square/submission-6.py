class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)
        matchsticks.sort(reverse=True)
        if total % 4 != 0:
            return False 

        target = sum(matchsticks) // 4 

        sides = [0, 0, 0, 0]

        def backtrack(k):

            nonlocal sides, target

            if k >= len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]


            seen = set()
            
            for i in range(len(sides)):
                if sides[i] in seen:
                    continue 
                seen.add(sides[i])
                if sides[i] + matchsticks[k] > target:
                    continue 
                sides[i] += matchsticks[k]
                res = backtrack(k + 1)
                sides[i] -= matchsticks[k]
                if res:
                    return True 

                if sides[i] == 0:
                    break

            return False 

        return backtrack(0)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        curr = []
        n = len(candidates)

        def backtrack(i, amount):
            nonlocal n

            if amount == 0:
                res.append(curr.copy())
                return 

            if amount < 0:
                return 

            if i == n:
                return 

            curr.append(candidates[i])
            backtrack(i + 1, amount - candidates[i])
            curr.pop()
            j = i + 1
            while j < n and candidates[j] == candidates[j - 1]:
                j += 1 
            
            backtrack(j, amount)

        backtrack(0, target)
        return res 
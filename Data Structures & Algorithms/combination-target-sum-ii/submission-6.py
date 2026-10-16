class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res = []
        curr = []

        def backtrack(i, total):

            if total > target: return 
            if total == target:
                res.append(curr.copy())
                return 

            if i == len(candidates): return 

            curr.append(candidates[i])
            total += candidates[i]

            backtrack(i + 1, total)

            curr.pop()
            total -= candidates[i]

            j = i + 1 
            while j < len(candidates) and candidates[j - 1] == candidates[j]:
                j += 1 

            backtrack(j, total)

        backtrack(0, 0)
        return res 
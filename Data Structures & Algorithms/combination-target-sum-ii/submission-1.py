class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        combination = []
        def backtrack(start, total):
            if total > target:
                return 
            if total == target:
                res.append(combination.copy())
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                total += candidates[i]
                combination.append(candidates[i])
                backtrack(i + 1, total)
                total -= candidates[i]
                combination.pop()

        backtrack(0, 0)
        return res 

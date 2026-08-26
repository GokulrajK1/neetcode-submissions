class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(total, i):
           
            if total == target:
                res.append(curr.copy())
                return

            if total > target:
                return 

            if i == len(candidates):
                return 

            curr.append(candidates[i])
            backtrack(total + candidates[i], i + 1)
            curr.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[j - 1]:
                j += 1
            backtrack(total, j)

        backtrack(0, 0)
        return res

            